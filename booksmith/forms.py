from django import forms
from .models import Book


class BookListingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "publication_date": forms.DateInput(attrs={
                "type": "date",
            }),
            "description": forms.Textarea(attrs={
                "rows": 5,
                "cols": 10,
            }),
        }