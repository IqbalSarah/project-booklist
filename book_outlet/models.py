from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        # verbose_name="xyz"
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.street}"

    class Meta:
        # verbose_name="xyz"
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books"
    )
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, blank=True)
    published_countries = models.ManyToManyField(Country)

    def save(self, *args, **kwargs):
        self.title = self.title.title()
        self.slug = slugify(self.title)  # for shell
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title}"
