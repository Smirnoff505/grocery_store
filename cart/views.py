from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import Cart, ProductInCart
from cart.serializers import CartSerializer, ProductSerializer, UpdateProductSerializer


class AddProductAPIView(generics.CreateAPIView):
    """Добавление продукта в корзину пользователя"""
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner=self.request.user.pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        product_in_cart, created = ProductInCart.objects.get_or_create(
            cart=cart,
            product=validated_data['product'],
        )

        if created:
            message = "Продукт добавлен в корзину."
        else:
            message = "Продукт уже был добавлен в корзину."

        return Response({"message": message}, status=status.HTTP_201_CREATED)


class UpdateProductAPIView(generics.UpdateAPIView):
    """Обновление количества продукта в корзине"""
    serializer_class = UpdateProductSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner=self.request.user.pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        product_in_cart = ProductInCart.objects.filter(cart=cart, product=validated_data['product']).first()

        if product_in_cart and validated_data['quantity'] > 1:
            # Обновляем количество продукта
            product_in_cart.quantity = validated_data['quantity']
            product_in_cart.save()
        else:
            return Response({'message': 'Данные не корректны'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Количество продукта изменено'}, status=status.HTTP_200_OK)


class DeleteProductAPIView(generics.DestroyAPIView):
    """Удаление продукта из корзины"""
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner=self.request.user.pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        ProductInCart.objects.filter(cart=cart, product=validated_data['product']).delete()

        return Response({'message': "Продукт удален из корзины"}, status.HTTP_204_NO_CONTENT)


class CartListAPIView(generics.ListAPIView):
    """Просмотр своей корзины пользователем"""
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем ID текущего пользователя из объекта request
        user_id = self.request.user.id
        # Фильтруем корзины по владельцу
        return Cart.objects.filter(owner=user_id)


class ProductInCartDestroyAPIView(generics.DestroyAPIView):
    """Удаление всех товаров из корзины"""
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        cart = Cart.objects.get(owner=self.request.user.pk)

        # Удаляем все продукты связанные с корзиной пользователя
        ProductInCart.objects.filter(cart=cart).delete()

        message = 'Корзина очищена'
        return Response({"message": message}, status=status.HTTP_204_NO_CONTENT)
