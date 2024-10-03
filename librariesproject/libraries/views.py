from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .forms import LibraryForm
from .models import Library

# Create your views here.

class LibraryList(ListView):
    model = Library
    template_name = "index.html.django"
    context_object_name = "libraries"

class LibraryDetail(DetailView):
    model = Library
    template_name = "detail.html.django"
    context_object_name = "library"

class LibraryCreate(SuccessMessageMixin, CreateView):
    model = Library
    template_name = "add.html.django"
    fields = LibraryForm.Meta.fields
    success_url = reverse_lazy("home")
    success_message = "%(name)s was created successfully!"

class LibraryUpdate(SuccessMessageMixin, UpdateView):
    model = Library
    template_name = "edit.html.django"
    fields = LibraryForm.Meta.fields
    success_url = reverse_lazy("home")
    success_message = "%(name)s was updated successfully!"

class LibraryDelete(SuccessMessageMixin, DeleteView):
    model = Library
    template_name = "delete.html.django"
    success_url = reverse_lazy("home")
    success_message = "Library was deleted successfully!"
