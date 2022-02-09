from rest_framework import serializers

from .models import HashTag, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'image', 'price', 'list_price', 'discount', 'hashtag', 'hashtag_content', 'sold_out')

    def validate(self, obj):
        try:
            if obj['price'] < 0 or obj['price'] > obj['list_price']:
                raise serializers.ValidationError("check the price!")
        except KeyError:
            pass
        return obj

class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ['content']
