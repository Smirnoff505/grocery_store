from django.contrib import admin

from cart.models import Cart, ProductInCart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner',)


@admin.register(ProductInCart)
class ProductInCartAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity',)
