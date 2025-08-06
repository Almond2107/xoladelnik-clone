from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

@login_required
def profile(request):
    """Display current user profile page."""
    return render(request, "profile.html")



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def product_single(request):
    return render(request, 'product-single.html')

def shop(request):
    return render(request, 'shop.html')

def wishlist(request):
    return render(request, 'wishlist.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Form to'g'ri bo'lsa — foydalanuvchi yaratish logikasi
            return redirect('login')  # yoki boshqa sahifaga yo'naltirish
        else:
            # Form xatoliklari bilan sahifani qayta chizish
            return render(request, 'auth/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'auth/register.html', {'form': form})
