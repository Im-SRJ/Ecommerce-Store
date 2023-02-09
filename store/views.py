from django.shortcuts import render

from .models import Category, Product

# Create your views here.

def categories(request):
    categories = Category.objects.all()
    return {"categories":categories}

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products})
