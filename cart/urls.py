from django.urls import path

from cart.apps import CartConfig
from cart.views import CartListAPIView, ProductInCartDestroyAPIView, AddProductAPIView, DeleteProductAPIView, \
    UpdateProductAPIView

app_name = CartConfig.name

urlpatterns = [
    path('list-cart/', CartListAPIView.as_view(), name='list-cart'),
    path('empty-cart/', ProductInCartDestroyAPIView.as_view(), name='empty-cart'),
    path('add-product/', AddProductAPIView.as_view(), name='add-prodict-cart'),
    path('delete-product/', DeleteProductAPIView.as_view(), name='delete-product-cart'),
    path('update-product/', UpdateProductAPIView.as_view(), name='update-product-cart'),
]
