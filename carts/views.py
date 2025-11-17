from django.shortcuts import render
from rest_framework import generics,permissions,serializers
from .models import Cart
from .serializers import CartSerializer
from products.models import Product
from products.permissions import IsCustomer
# Create your views here.



class CartListAndAddView(generics.ListCreateAPIView):
    serializer_class=CartSerializer
    permission_classes=[permissions.IsAuthenticated,IsCustomer]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        product_id=self.request.data.get('product')
        quantity=int(self.request.data.get('quantity',1))
        
        try:
            product=Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError({product_id:"product does not exist"})
        
        if quantity>product.stock:
            raise serializers.ValidationError({"detail": "Not enough stock available."})

        cart_item,created=Cart.objects.get_or_create(
            user=self.request.user,
            product=product,
            defaults={'quantity':quantity}
        )

        if not created:
            cart_item.quantity=cart_item.quantity+quantity
            cart_item.save()
        
        return cart_item
    

class CartUpdateOrDeleteOrRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer
    permission_classes=[permissions.IsAuthenticated,IsCustomer]
    def perform_update(self, serializer):
        serializer.save(Customer=self.request.user)
        