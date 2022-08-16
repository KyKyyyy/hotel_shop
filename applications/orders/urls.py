from rest_framework.routers import DefaultRouter

from applications.orders.views import CartItemView, OrderView

router = DefaultRouter()
router.register('cart', CartItemView)
router.register('', OrderView)

urlpatterns = []

# urlpatterns += router.urls
urlpatterns.extend(router.urls)