from rest_framework import serializers
from .models import Product, ProductVariant, ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
