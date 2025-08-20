from rest_framework import generics, permissions
from .models import BlogPost, BlogCategory, Tag, Comment
from blog.serializer.blog import BlogPostSerializer, BlogCategorySerializer, TagSerializer, CommentSerializer
from django.shortcuts import render, get_object_or_404



# ----------------- BlogPost -----------------
class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().select_related('user', 'category').prefetch_related('tags', 'comments')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all().select_related('user', 'category').prefetch_related('tags', 'comments')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# ----------------- BlogCategory -----------------
class BlogCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BlogCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




# ----------------- Tag -----------------
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TagRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# ----------------- Comment -----------------
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().select_related('user', 'post')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().select_related('user', 'post')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
