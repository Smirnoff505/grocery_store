from rest_framework import generics
from rest_framework.response import Response

from cart.models import Cart
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """Создание корзины при регистрации пользователя"""
        user = serializer.save()
        Cart.objects.create(owner=user)
        return Response(serializer.data)
