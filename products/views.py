from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer,ListProductSerializer
from .permissions import IsCustomer,IsSeller
from rest_framework import generics,permissions,exceptions
# Create your views here.


class ListAndAddProductView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes=[permissions.IsAuthenticated,IsCustomer]

        elif self.request.method == 'POST':
            permission_classes=[permissions.IsAuthenticated,IsSeller]
        else:
            permission_classes=[permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListProductSerializer
        return ProductSerializer
    def perform_create(self, serializer):
        serializer.save(Seller=self.request.user)


class RetrieveAndUpdateAndDestroyProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get_permissions(self):
        if self.request.method == 'GET':  # covers GET, HEAD, OPTIONS
            permission_classes = [permissions.IsAuthenticated, IsCustomer]
        else:  # for PUT, PATCH, DELETE
            permission_classes = [permissions.IsAuthenticated, IsSeller]

        return [permission() for permission in permission_classes]
    def perform_update(self, serializer):
        serializer.save(Seller=self.request.user)
        
    def perform_destroy(self, instance):
        if instance.Seller != self.request.user:
            raise exceptions.PermissionDenied("You do not have permission to delete this object.")
        instance.delete()