from rest_framework import serializers
from .models import  Product

class ProductSerializer(serializers.ModelSerializer):
    Seller=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Product
        fields='__all__'

class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','price']