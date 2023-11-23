from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "booksmith"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("book-listing-form/", views.BookListingFormView.as_view(), name="book_listing_form"),
    path("book-detail/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
]
