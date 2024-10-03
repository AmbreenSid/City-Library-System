from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Author
from .forms import AuthorForm

# Create your views here.

class AuthorList(ListView):
    model = Author
    template_name = "author-index.html.django"
    context_object_name = "authors"

class AuthorDetail(DetailView):
    model = Author
    template_name = "author-detail.html.django"
    context_object_name = "author"

class AuthorCreate(SuccessMessageMixin, CreateView):
    model = Author
    template_name = "add-author.html.django"
    fields = AuthorForm.Meta.fields
    success_url = reverse_lazy("authors-home")
    success_message = "%(name)s was created successfully!"

class AuthorUpdate(SuccessMessageMixin, UpdateView):
    model = Author
    template_name = "edit-author.html.django"
    fields = AuthorForm.Meta.fields
    success_url = reverse_lazy("authors-home")
    success_message = "%(name)s was updated successfully!"

class AuthorDelete(SuccessMessageMixin, DeleteView):
    model = Author
    template_name = "delete-author.html.django"
    success_url = reverse_lazy("authors-home")
    success_message = "Author was deleted successfully!"
