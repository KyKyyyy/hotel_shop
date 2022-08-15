from django.shortcuts import render

# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from applications.orders.models import  CartItem
from applications.orders.serializers import  CartItemSerializer


class CartItemView(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(cart=user.carts.first())
        return queryset
