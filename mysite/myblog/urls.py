from django.contrib import admin
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    UserPostListView,
                    UserCommentListView,
                    search,
                    register)

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
    path("userposts/", UserPostListView.as_view(), name="userposts"),
    path("usercomments/", UserCommentListView.as_view(), name="usercomments"),
    path("search/", search, name="search"),
    path('register/', register, name='register'),
]
