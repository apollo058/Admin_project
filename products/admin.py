from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product, HashTag


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'sold_out', 'discount', 'hashtag_content','image_view', 'created')
    list_display_links = ('name',)
    filter_horizontal = ('hashtag',)
    readonly_fields = ('discount',)
    search_fields = ('name',)

    def image_view(self, obj):
        try:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100"/>')
        except ValueError:
            return "No Image"

@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = ['content']

