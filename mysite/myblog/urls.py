from django.contrib import admin
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    UserPostListView,
                    search)

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
    path("userposts/", UserPostListView.as_view(), name="userposts"),
    path("search/", search, name="search"),
]
