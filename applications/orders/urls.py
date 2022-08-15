from rest_framework.routers import DefaultRouter

from applications.orders.views import CartItemView

router = DefaultRouter()
router.register('cart', CartItemView)


urlpatterns = []

# urlpatterns += router.urls
urlpatterns.extend(router.urls)