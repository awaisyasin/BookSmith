from django.db import models
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from accounts.models import CustomUser

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.CharField(max_length=1000)
    cover_image = models.ImageField()

    def __str__(self):
        return f"{self.title} ({self.author})"

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="reviews", null=True)
    review = models.CharField(max_length=1000)
    book = models.ForeignKey(Book, related_name="reviews", on_delete=models.CASCADE)

class Favourite(models.Model):
    user = models.ManyToManyField(CustomUser)
    book = models.ManyToManyField(Book)

class Collection(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="collection")
    book = models.ManyToManyField(Book)