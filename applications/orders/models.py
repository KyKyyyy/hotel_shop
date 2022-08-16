from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.db.models.signals import post_delete
from django.dispatch import receiver

from applications.hotels.models import Hotels

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')

    def __str__(self):
        return self.user.email


class CartItem(models.Model):  # продукты в корзине
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,  related_name='cart_items')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.cart.id} {self.hotel}'



class Order(models.Model):
    CART_STATUS = (
        ('in_processing', 'in_processing'),
        ('completed', 'completed'),  # завершенный
        ('declined', 'declined')  # отклоненный
    )
    # product = models.ForeignKey(Product,
    #                             on_delete=models.CASCADE,
    #                             related_name='orders'
    #                             )
    customer = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 related_name='orders')
    # quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=CART_STATUS,
                              default='in_processing')
    address = models.TextField()
    number = models.TextField()
    first_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    info = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} ordered'
#
# from django.contrib.auth import get_user_model
# from django.db import models
#
# # Create your models here.
# from applications.hotels.models import Hotels
#
# User = get_user_model()
#
#
# class Order(models.Model):
#     item = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='product')
#     amount = models.PositiveIntegerField()
#     # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     total_price = models.PositiveIntegerField(blank=True)
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
#
#     def save(self, *args, **kwargs):
#         self.total_price = self.item.price * self.amount
#         super().save(*args, **kwargs)
