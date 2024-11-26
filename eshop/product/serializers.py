from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Product
        fields =  ['id', 'name', 'description', 'price', 'brand', 'category', 'ratings', 'stock', 'image']