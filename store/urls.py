from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("book/<slug:slug>", views.product_detail, name="product_detail"),
    path("<slug:slug>", views.category_detail, name="category_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
