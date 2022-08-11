from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

User = get_user_model()


class Hotels(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(blank=True, null=True)
    free_place = models.PositiveIntegerField()
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], default=1
    )

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='hotels')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='images')


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='Владелец лайка')
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name='likes', verbose_name='Товар')
    like = models.BooleanField('лайк', default=False)

    def __str__(self):
        return f'{self.product} {self.like}'