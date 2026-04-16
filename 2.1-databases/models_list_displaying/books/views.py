from datetime import datetime

from django.shortcuts import render
from books.models import Book


def books_view(request, pub_date=None):
    template = "books/books_list.html"
    prev_date = None
    next_date = None
    if pub_date:
        dt = datetime.strptime(pub_date, "%Y-%m-%d").date()
        books = Book.objects.filter(pub_date=dt)
        prev_date_obj = (
            Book.objects.filter(pub_date__lt=dt).order_by("-pub_date").first()
        )
        next_date_obj = (
            Book.objects.filter(pub_date__gt=dt).order_by("pub_date").first()
        )

        if prev_date_obj:
            prev_date = prev_date_obj.pub_date
        if next_date_obj:
            next_date = next_date_obj.pub_date
        print({pub_date})
    else:
        books = Book.objects.all().order_by("pub_date")
    context = {"books": books, "prev_date": prev_date, "next_date": next_date}
    return render(request, template, context)
