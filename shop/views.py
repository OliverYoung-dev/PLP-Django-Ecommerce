from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, slug, product_id):
    product = get_object_or_404(Product, slug=slug, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id, slug):
    cart = cart(request)
    product = get_object_or_404(Product, id=product_id, slug=slug)
    cart.add(product=product)
    order, created = Order.objects.get_or_create(user=request.user, ordered=False)
    order_item, created = OrderItem.objects.get_or_create(product=product, order=order)
    order_item.quantity += 1
    order_item.save()
    return redirect('cart')

def cart_detail(request):
    order = Order.objects.filter(user=request.user, ordered=False).first()
    return render(request, 'shop/cart_detail.html', {'order': order})

@login_required
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order = Order.objects.get(user=request.user)
    order_item = OrderItem.objects.get(order=order, product=product)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect('cart')

@login_required
def cart(request):
    order = Order.objects.get(user=request.user)
    return render(request, 'shop/cart.html', {'order': order})

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user)
    # Handle checkout process, integrate payment gateway here
    return render(request, 'shop/checkout.html', {'order': order})

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

# Handle user registration, integrate with Django's UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
    if request.user.is_authenticated:
        return redirect('product_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})
