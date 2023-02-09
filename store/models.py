from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("category_detail", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default="admin")
    category = models.ForeignKey(
        Category, related_name="product", on_delete=models.CASCADE
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="Images/")
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="product_creator"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_by",)

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.slug])

    def __str__(self):
        return self.title
