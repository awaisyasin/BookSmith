from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse
import requests
from .forms import BookListingForm
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
def home_view(request):
    response = requests.get("https://openlibrary.org/search.json", params="money")
    data = response.json()

    num_book_to_show = 10

    books = [
        {
            "title": book.get("title", ""),
            "author": book.get("author", []),
            "cover": book.get("cover", "")
        }
        for book in data.get("docs", [])[:num_book_to_show]
    ]
    print(books)

    return render(request, "booksmith/home.html", {"books": books})


class HomeView(ListView):
    model = Book
    template_name = "booksmith/home.html"
    context_object_name = "books"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            return Book.objects.filter(title__icontains=query)
        else:
            return super().get_queryset()


class BookListingFormView(CreateView):
    model = Book
    form_class = BookListingForm
    template_name = "booksmith/book-listing-form.html"
    success_url = reverse_lazy("booksmith:home")


class BookDetailView(DetailView):
    model = Book
    template_name = "booksmith/book-detail.html"