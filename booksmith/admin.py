from django.contrib import admin
from .models import Book, Genre, Review, Favourite, Collection

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    ordering = ["name"]

admin.site.register(Book)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review)
admin.site.register(Favourite)
admin.site.register(Collection)