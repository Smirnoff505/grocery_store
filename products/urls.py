from django.urls import path

from products.apps import ProductsConfig
from products.views import CategoryListAPIView, ProductListAPIView

app_name = ProductsConfig.name

urlpatterns = [
    # Категории
    path('list/', CategoryListAPIView.as_view(), name='list-category'),

    # Продукты
    path('productlist/', ProductListAPIView.as_view(), name='list-products')
]
