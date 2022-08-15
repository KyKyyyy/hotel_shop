# from django.contrib.auth import get_user_model
# from django.db import models
#
# # Create your models here.
# from django.db.models.signals import post_delete
# from django.dispatch import receiver
#
# from applications.hotels.models import Hotels
#
# User = get_user_model()
#
#
# class Cart(models.Model):
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE,
#                              related_name='carts'
#                              )
#     total_cost = models.DecimalField(max_digits=100, decimal_places=2, default=0)
#
#     def __str__(self):
#         return self.user.email
#
#
# class CartItem(models.Model):  # продукты в корзине
#     cart = models.ForeignKey(Cart,
#                              on_delete=models.CASCADE,
#                              related_name='cart_items'
#                              )
#     hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='cart_items')
#     quantity = models.PositiveIntegerField()
#     total_cost = models.DecimalField(max_digits=100,
#                                      decimal_places=2,
#                                      default=0)
#
#     def __str__(self):
#         return f'{self.cart.id} {self.hotel}'
#
#     def save(self, *args, **kwargs):
#         self.total_cost = self.hotel.free_place * self.quantity
#
#         try:
#             cartitem = CartItem.objects.get(id=self.id)
#             cartitem.cart.total_cost = cartitem.cart.total_cost - \
#                                        cartitem.total_cost + \
#                                        self.total_cost
#             cartitem.cart.save()
#         except CartItem.DoesNotExist:
#             self.cart.total_cost += self.total_cost
#             self.cart.save()
#
#         super(CartItem, self).save()
#
#
# @receiver(post_delete, sender=CartItem)
# def delete_signal(sender, instance, **kwargs):
#     instance.cart.total_cost -= instance.total_cost
#     instance.cart.save()
#
