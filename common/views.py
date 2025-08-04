from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    """Homepage view that renders the main landing page."""
    return render(request, "index.html")


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class BlogSingleView(TemplateView):
    template_name = 'blog-single.html'

class CartView(TemplateView):
    template_name = 'cart.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class ProductSingleView(TemplateView):
    template_name = 'product-single.html'

class ShopView(TemplateView):
    template_name = 'shop.html'

class WishlistView(TemplateView):
    template_name = 'wishlist.html'
