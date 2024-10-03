from django.urls import path
from .views import AuthorList, AuthorDetail, AuthorCreate, AuthorUpdate, AuthorDelete

urlpatterns = [
    path("", AuthorList.as_view(), name="authors-home"),
    path("<int:pk>", AuthorDetail.as_view(), name = "author-detail"),
    path("add", AuthorCreate.as_view(), name = "add-author"),
    path("edit/<int:pk>", AuthorUpdate.as_view(), name = "edit-author"),
    path("delete/<int:pk>", AuthorDelete.as_view(), name = "delete-author")
]
