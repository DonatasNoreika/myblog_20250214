from django.contrib import admin
from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    UserPostListView,
                    UserCommentListView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    CommentUpdateView,
                    CommentDeleteView,
                    search,
                    register)

urlpatterns = [
    path("userposts/", UserPostListView.as_view(), name="userposts"),
    path("usercomments/", UserCommentListView.as_view(), name="usercomments"),
    path("search/", search, name="search"),
    path('register/', register, name='register'),
    path("", PostListView.as_view(), name="posts"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post"),
    path('posts/new', PostCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/update", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path("comments/<int:pk>/update", CommentUpdateView.as_view(), name="comment_update"),
    path("comments/<int:pk>/delete", CommentDeleteView.as_view(), name="comment_delete"),
]
