from django.urls import path
from .views import (
    PostListView, PostCreateView, PostUpdateView, PostDeleteView, post_detail
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/new/", PostCreateView.as_view(), name="post_create"),
    path("post/<slug:slug>/", post_detail, name="post_detail"),
    path("post/<slug:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("post/<slug:slug>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
