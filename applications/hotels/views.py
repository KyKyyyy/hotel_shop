from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.hotels.models import Hotels, Like
from applications.hotels.permissions import CustomIsAdmin
from applications.hotels.serializers import HotelSerializer


class SetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


class HotelsView(ModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
    pagination_class = SetPagination
    permission_classes = [CustomIsAdmin]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    # filterset_fields = ['rating', 'name']
    ordering_fields = ['name', 'id']
    search_fields = ['name', 'description']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk, *args, **kwargs):
        # print(pk)
        try:
            like_object, _ = Like.objects.get_or_create(owner=request.user, product_id=pk)
            like_object.like = not like_object.like
            like_object.save()
            status = 'liked'

            if like_object.like:
                return Response({'status': status})
            status = 'unliked'
            return Response({'status': status})
        except:
            return Response('Нет такого продукта!')
