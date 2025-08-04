from django.urls import path
from common.views import (HomeView, AboutView, BlogSingleView, BlogView, 
                          CartView, CheckoutView, ContactView, 
                          ProductSingleView, ShopView, WishlistView,
)



urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("blog-single/", BlogSingleView.as_view(), name="blog-single"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("cart/", CartView.as_view(), name="cart"),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("product-single/", ProductSingleView.as_view(), name="product-single"),
    path("shop/", ShopView.as_view(), name="shop"),
    path("wishlist/", WishlistView.as_view(), name="wishlist")

]
