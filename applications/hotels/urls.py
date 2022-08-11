from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.hotels.views import HotelsView

router = DefaultRouter()
router.register('', HotelsView)

urlpatterns = [
    path('', include(router.urls)),


]