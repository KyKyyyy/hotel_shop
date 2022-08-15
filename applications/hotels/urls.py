from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.hotels.views import HotelsView, CommentView

router = DefaultRouter()
router.register('', HotelsView)
router.register('comment', CommentView)

urlpatterns = [
    path('', include(router.urls)),


]