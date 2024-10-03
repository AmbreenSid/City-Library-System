from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

urlpatterns = [
    path("", BookList.as_view(), name="books-home"),
    path("<int:pk>", BookDetail.as_view(), name = "book-detail"),
    path("add", BookCreate.as_view(), name = "add-book"),
    path("edit/<int:pk>", BookUpdate.as_view(), name = "edit-book"),
    path("delete/<int:pk>", BookDelete.as_view(), name = "delete-book")
] 