from django.urls import path
from .views import (
    ProductCategoryListCreateView,
    ProductCategoryRetrieveUpdateDestroyView,
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
    ProductVariantListCreateView,
    ProductVariantRetrieveUpdateDestroyView,
)

urlpatterns = [
    # Category
    path("categories/", ProductCategoryListCreateView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", ProductCategoryRetrieveUpdateDestroyView.as_view(), name="category-detail"),

    # Product
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    path("products/<int:pk>/", ProductRetrieveUpdateDestroyView.as_view(), name="product-detail"),

    # ProductVariant
    path("variants/", ProductVariantListCreateView.as_view(), name="variant-list-create"),
    path("variants/<int:pk>/", ProductVariantRetrieveUpdateDestroyView.as_view(), name="variant-detail"),
]
