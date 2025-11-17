from django.shortcuts import render
from .models import Order,OrderItem
from .serializers import OrderSerializer,OrderItemSerializer
from rest_framework import generics,permissions,exceptions
from products.permissions import IsCustomer,IsSeller
from django.db import transaction
# Create your views here.


class OrderListAndCreateView(generics.ListCreateAPIView):
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated,IsCustomer]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        user = self.request.user
        cart_items = user.cart_set.all()

        if not cart_items.exists():
            raise exceptions.ValidationError("Cart is empty!")

        # Sum the total_price of all cart items
        total = sum(item.total_price for item in cart_items)

        with transaction.atomic():
            # Save order with user and total
            orderObj=serializer.save(user=user, total=total)
            for item in cart_items:
                OrderItem.objects.create(
                    order=orderObj,
                    product=item.product,
                    Seller=item.product.Seller,
                    quantity=item.quantity,
                    price_at_purchased=item.product.price,
                )
            # Clear the cart after creating the order
            cart_items.delete()


class OrderRetrieveUpdateAndDestroyView(generics.ListAPIView):
    serializer_class=OrderItemSerializer
    permission_classes=[permissions.IsAuthenticated,IsCustomer]
    def get_queryset(self):
        order_id = self.kwargs['pk']  # usually from URL
        return OrderItem.objects.filter(order__user=self.request.user, order__id=order_id)
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         permission_classes=[permissions.IsAuthenticated,IsCustomer]
    #     elif self.request.method == 'PUT':
    #         permission_classes=[permissions.IsAuthenticated,IsSeller]
    #     else :
    #         permission_classes=[permissions.IsAuthenticated]
        
    #     return [permission() for permission in permission_classes]
    
    # def perform_update(self, serializer):
    #     status=serializer.data['status']
    #     serializer.save(user=self.request.user,status=status)