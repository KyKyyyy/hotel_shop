from rest_framework import serializers

from applications.hotels.models import Hotels, Image, Comment


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['image']


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    text = serializers.CharField(max_length=400)
    hotel = serializers.ReadOnlyField(source='hotel.id')

    class Meta:
        model = Comment
        fields = '__all__'

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     print(rep)
    #     rep['text'] = 'hiiii'
    #     return rep


class HotelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    images = ImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Hotels
        fields = '__all__'

    def create(self, validated_data):
        requests = self.context.get('request')
        images = requests.FILES
        for i in range(10):
            hotel = Hotels.objects.create(**validated_data)
        for image in images.getlist('images'):
            Image.objects.create(hotel=hotel, image=image)
        return hotel

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['likes'] = instance.likes.filter(like=True).count()
        return representation


class RatingSerializer(serializers.Serializer):
    rating = serializers.IntegerField(required=True, min_value=1, max_value=5)
