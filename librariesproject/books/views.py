from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Book
from .forms import BookForm

# Create your views here.

class BookList(ListView):
    model = Book
    template_name = "book-index.html.django"
    context_object_name = "books"

class BookDetail(DetailView):
    model = Book
    template_name = "book-detail.html.django"
    context_object_name = "book"

class BookCreate(SuccessMessageMixin, CreateView):
    model = Book
    template_name = "add-book.html.django"
    fields = BookForm.Meta.fields
    success_url = reverse_lazy("books-home")
    success_message = "%(name)s was created successfully!"

class BookUpdate(SuccessMessageMixin, UpdateView):
    model = Book
    template_name = "edit-book.html.django"
    fields = BookForm.Meta.fields
    success_url = reverse_lazy("books-home")
    success_message = "%(name)s was updated successfully!"

class BookDelete(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = "delete-book.html.django"
    success_url = reverse_lazy("books-home")
    success_message = "Book was deleted successfully!"
