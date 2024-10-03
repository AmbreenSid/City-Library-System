from django.urls import path
from .views import LibraryList, LibraryDetail, LibraryCreate, LibraryUpdate, LibraryDelete

urlpatterns = [
    path("", LibraryList.as_view(), name = "home"),
    path("<int:pk>", LibraryDetail.as_view(), name = "detail"),
    path("add", LibraryCreate.as_view(), name = "add"),
    path("edit/<int:pk>", LibraryUpdate.as_view(), name = "edit"),
    path("delete/<int:pk>", LibraryDelete.as_view(), name = "delete")
]
