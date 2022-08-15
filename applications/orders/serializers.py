from rest_framework import serializers

from applications.orders.models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        # fields = '__all__'
        exclude = ['cart']

    def create(self, validated_data):
        user = self.context.get('request').user
        cart, _ = Cart.objects.get_or_create(user=user)

        cart_item = CartItem.objects.create(
            cart=cart,
            hotel=validated_data['hotel'],
            quantity=validated_data['quantity']
        )

        quntity_order = validated_data['quantity']
        hotel = validated_data['hotel']
        hotel_quantity = hotel.free_place

        if quntity_order > hotel_quantity:
            raise serializers.ValidationError(f'Нет такого количества, есть только {hotel_quantity}')
        hotel.free_place -= quntity_order
        hotel.save()

        return cart_item