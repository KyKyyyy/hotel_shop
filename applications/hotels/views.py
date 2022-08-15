from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from applications.hotels.models import Hotels, Like, Comment, Favorite, Rating
from applications.hotels.permissions import CustomIsAdmin
from applications.hotels.serializers import HotelSerializer, CommentSerializer, RatingSerializer


class SetPagination(PageNumberPagination):
    page_size = 4
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
        try:
            like_object, _ = Like.objects.get_or_create(owner=request.user, hotel_id=pk)
            like_object.like = not like_object.like
            like_object.save()
            status = 'liked'

            if like_object.like:
                return Response({'status': status})
            status = 'unliked'
            return Response({'status': status})
        except:
            return Response('Нет такого продукта!')

    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk, *args, **kwargs):
        try:
            favorite_object, _ = Favorite.objects.get_or_create(owner=request.user, hotel_id=pk)
            favorite_object.like = not favorite_object.like
            favorite_object.save()
            status = 'added'

            if favorite_object.like:
                return Response({'status': status})
            status = 'deleted'
            return Response({'status': status})
        except:
            return Response('Нет такого продукта!')

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk, *args, **kwargs):
        serializers = RatingSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        obj, _ = Rating.objects.get_or_create(hotel_id=pk,
                                              owner=request.user)
        obj.rating = request.data['rating']
        obj.save()
        return Response(request.data, status=201)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [IsAuthenticated]
        elif self.action == 'like' or self.action == 'rating':
            permissions = [IsAuthenticated]
        else:
            permissions = [CustomIsAdmin]

        return [p() for p in permissions]


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

