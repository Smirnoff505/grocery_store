from django.db import models

from config import settings
from products.models import Product


class Cart(models.Model):
    """Модель корзины"""
    owner = models.OneToOneField(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE,
                                 related_name='owner',
                                 verbose_name='Корзина')

    def __str__(self):
        return self.owner.email

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class ProductInCart(models.Model):
    """Модель продуктов корзины"""
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart', verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product', verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return self.cart.owner.email

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'
        unique_together = ('cart', 'product')


