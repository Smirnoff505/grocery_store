from rest_framework import generics

from products.models import Category, Product
from products.pagination import CategoryListPagination, ProductListPagination
from products.serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(generics.ListAPIView):
    pagination_class = CategoryListPagination
    """Список всех категорий и подкатегорий"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProductListAPIView(generics.ListAPIView):
    pagination_class = ProductListPagination
    """Список всех продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()