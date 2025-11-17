from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsManager
from rest_framework.response import Response
# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]

class ManagerView(APIView):
    permission_classes=[IsAuthenticated,IsManager]

    def get(self, request):
        return Response({"message": "Hello Manager!"})