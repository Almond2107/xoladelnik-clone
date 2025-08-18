from rest_framework import serializers
from blog.models import BlogPost, BlogCategory, Tag, Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'is_active']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'text', 'is_active', 'created_at', 'updated_at']

class BlogPostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    category = BlogCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=BlogCategory.objects.all(), source='category', write_only=True, required=False
    )
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, source='tags', write_only=True, required=False
    )
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content', 'image', 'status', 'is_featured',
            'published_at', 'user', 'category', 'category_id', 'tags', 'tag_ids', 'comments',
            'created_at', 'updated_at'
        ]
