from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg, Max, Min


# Create your views here.
def index(request):
    books = Book.objects.all()
    total_books = books.count()
    book_ag = books.aggregate(Avg("rating"))

    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_books": total_books,
            "avg_rating": book_ag,
        },
    )


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "isbestsell": book.is_bestselling,
        },
    )

    # total_books = len(books)
    # total_rating = 0
    # for b in books:
    #     total_rating += b.rating
    # avg = total_rating / total_books
