from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# Create your views here.


def categories(request):
    categories = Category.objects.all()
    return {"categories": categories}


def home(request):
    products = Product.objects.all()
    return render(request, "store/home.html", {"products": products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, "store/product/detail.html", {"product": product})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    return render(
        request,
        "store/product/category.html",
        {"category": category, "products": products},
    )
