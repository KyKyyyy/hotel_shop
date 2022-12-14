# Generated by Django 4.1 on 2022-08-11 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotels', '0004_remove_hotels_stars_hotels_rating_image_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False, verbose_name='лайк')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='hotels.hotels', verbose_name='Товар')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Владелец лайка')),
            ],
        ),
    ]
