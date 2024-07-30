from rest_framework import serializers

from cart.models import ProductInCart, Cart


class ProductInCartSerializer(serializers.ModelSerializer):
    product_title = serializers.CharField(source='product.title')
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='product.price')

    class Meta:
        model = ProductInCart
        fields = ('id', 'product', 'product_title', 'quantity', 'product_price',)


class CartSerializer(serializers.ModelSerializer):
    # Вложенный список продуктов
    products = ProductInCartSerializer(many=True, source='cart')

    # Дополнительные вычисляемые поля количества и итоговой цены продуктов
    count = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ('id', 'owner', 'count', 'total_price', 'products',)

    def get_count(self, obj):
        """Количество всех продуктов в корзине"""
        return sum([product.quantity for product in obj.cart.all()])

    def get_total_price(self, obj):
        """Итоговая цена всех продуктов в корзине"""
        return sum([product.product.price * product.quantity for product in obj.cart.all()])


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = ('product',)


class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInCart
        fields = ('product', 'quantity',)
