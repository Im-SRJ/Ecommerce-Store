from django.contrib import admin

from .models import Category, Product

# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "slug",
        "price",
        "category",
        "in_stock",
        "created_by",
    ]
    list_filter = ["in_stock", "is_active"]
    list_editable = ["price", "in_stock"]
    prepopulated_fields = {"slug": ("title",)}
