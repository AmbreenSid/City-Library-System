from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("name", "image", "pages", "genres", "author", "libraries")