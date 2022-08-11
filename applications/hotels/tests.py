# from django.test import TestCase
#
# # Create your tests here.
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.email')
#     images = ImageSerializer(many=True, read_only=True)
#     comments = CommentSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def create(self, validated_data):
#         requests = self.context.get('request')
#         images = requests.FILES
#         for i in range(10):
#             product = Product.objects.create(**validated_data)
#         for image in images.getlist('images'):
#             Image.objects.create(product=product, image=image)
#
#         send_product_info.delay(validated_data['name'])
#         return product
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         # print(instance.likes.filter(like=True).count())
#         representation['likes'] = instance.likes.filter(like=True).count()
#
#         rating_result = 0
#         for rating in instance.ratings.all():
#             rating_result += int(rating.rating)
#         try:
#             representation['rating'] = rating_result / instance.ratings.all().count()
#         except ZeroDivisionError:
#             # representation['rating'] = 0
#             pass
#         representation['best name'] = 'John'
#         return representation