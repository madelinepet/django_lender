# a function view controller that listens to the req
from django.shortcuts import render, get_object_or_404
from .models import Book


def books_list_view(request):
    # can't use dot notation on the left side of =, so use
    # __ (double underscore) instead,
    # Django reads it like "user.username"
    books = Book.objects.filter(user__username=request.user.username)
    context = {
        'books': books
    }

    return render(request, 'books/books_list.html', context=context)


def books_detail_view(request, pk=None):
    book = get_object_or_404(Book, id=pk, user__username=request.user.username)
    context = {
        'book': book,
    }
    return render(request, 'books/books_detail.html', context)
