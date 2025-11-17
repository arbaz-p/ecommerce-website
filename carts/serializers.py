from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    total_price=serializers.SerializerMethodField(read_only=True)
    price=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'

    def get_total_price(self,obj):
        return getattr(obj,'total_price',None)
    
    def get_price(self,obj):
        if hasattr(obj,'product') and obj.product:
            return obj.product.price
        return None