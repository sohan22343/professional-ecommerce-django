from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms 
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Cart
from django.db import transaction
from .models import Product, Cart, Order, Customer
from .forms import SignUpForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged In. "))
            return redirect('home')
        else:
            messages.success(request, ("Error. Please Try again. "))
            return redirect('login')
    
    else:
        return render(request, 'store/login.html', {})

def logout_user(request):
   logout(request)
   messages.success(request, ("You have been logged out...."))
   return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user
            user = authenticate(username=username, password=password )
            login(request, user)
            messages.success(request, ("You have registered successfully...."))
            return redirect('home')
        else:
            messages.success(request, ("whoops!there is a problem...."))
            return redirect('register')
        
    else:       
        return render(request, 'store/register.html', {'form':form})

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} added to your cart.")
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from your cart.")
    return redirect('view_cart')

@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Cart updated successfully.")
        else:
            cart_item.delete()
            messages.success(request, "Item removed from your cart.")
    return redirect('view_cart')

def about(request):
    return render(request, 'store/about.html')

# Payment Views
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    if not cart_items:
        messages.warning(request, "Your cart is empty.")
        return redirect('view_cart')
    return render(request, 'store/checkout.html')

@login_required
@transaction.atomic
def process_payment(request):
    if request.method != 'POST':
        messages.error(request, "Invalid request method.")
        return redirect('checkout')
    
    try:
        # Get existing customer (must exist in database)
        customer = Customer.objects.get(user=request.user)
        
        # Get cart items
        cart_items = Cart.objects.filter(user=request.user)
        if not cart_items:
            messages.error(request, "Your cart is empty.")
            return redirect('view_cart')
        
        # Create order for each product in cart
        for cart_item in cart_items:
            Order.objects.create(
                Customer=customer,  # Must match your model's field name (uppercase C)
                Product=cart_item.product,  # Must match your model's field name (uppercase P)
                quantity=cart_item.quantity,
                total=cart_item.total_price(),
                status=True
            )
        
        # Clear cart
        cart_items.delete()
        
        messages.success(request, "Order created successfully!")
        return redirect('payment_success')
    
    except Customer.DoesNotExist:
        messages.error(request, "Customer profile not found. Please contact support.")
        return redirect('checkout')
    except Exception as e:
        logger.error(f"Payment error: {str(e)}")
        messages.error(request, "Payment processing failed. Please try again.")
        return redirect('checkout')

def payment_success(request):
    return render(request, 'store/payment_success.html')

def payment_cancelled(request):
    messages.info(request, "store/Payment was cancelled.")
    return render(request, 'store/payment_cancelled.html')