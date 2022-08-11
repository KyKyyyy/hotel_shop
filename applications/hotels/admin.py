from django.contrib import admin

# Register your models here.
from applications.hotels.models import Hotels, Image

admin.site.register(Image)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class HotelAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]
    list_display = ['id', 'name', 'free_place', 'rating', ]


admin.site.register(Hotels, HotelAdmin)
