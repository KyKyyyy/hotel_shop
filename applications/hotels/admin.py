from django.contrib import admin

# Register your models here.
from applications.hotels.models import Hotels, Image, Like, Rating, Comment

admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Rating)
admin.site.register(Comment)


class ImageInAdmin(admin.TabularInline):
    model = Image
    fields = ['image']
    max_num = 5


class HotelAdmin(admin.ModelAdmin):
    inlines = [ImageInAdmin]
    list_display = ['id', 'name', 'free_place', 'rating', ]

    def count_like(self, obj):
        return obj.likes.filter(like=True).count()


admin.site.register(Hotels, HotelAdmin)
