from django.urls import path
from .views import (
    BlogPostListCreateAPIView, BlogPostRetrieveUpdateDestroyAPIView,
    BlogCategoryListCreateAPIView, BlogCategoryRetrieveUpdateDestroyAPIView,
    TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # BlogPost
    path('posts/', BlogPostListCreateAPIView.as_view(), name='blogpost-list'),
    path('posts/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blogpost-detail'),

    # BlogCategory
    path('categories/', BlogCategoryListCreateAPIView.as_view(), name='blogcategory-list'),
    path('categories/<int:pk>/', BlogCategoryRetrieveUpdateDestroyAPIView.as_view(), name='blogcategory-detail'),

    # Tag
    path('tags/', TagListCreateAPIView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag-detail'),

    # Comment
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]
