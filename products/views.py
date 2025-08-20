from rest_framework import generics
from .models import Product, ProductVariant, ProductCategory
from .serializers import (
    ProductSerializer,
    ProductVariantSerializer,
    ProductCategorySerializer,
)


# --- ProductCategory ---
class ProductCategoryListCreateView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


# --- Product ---
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# --- ProductVariant ---
class ProductVariantListCreateView(generics.ListCreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer


class ProductVariantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
