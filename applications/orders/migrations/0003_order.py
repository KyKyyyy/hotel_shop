# Generated by Django 4.1 on 2022-08-16 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_remove_cart_total_cost_remove_cartitem_total_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_processing', 'in_processing'), ('completed', 'completed'), ('declined', 'declined')], default='in_processing', max_length=20)),
                ('address', models.TextField()),
                ('number', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('info', models.TextField(blank=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
