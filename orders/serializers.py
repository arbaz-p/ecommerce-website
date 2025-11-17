from rest_framework import serializers
from .models import Order,OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['user','total','status','created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItem
        fields='__all__'
        read_only_fields=['order','product','Seller','quantity','price_at_purchased']