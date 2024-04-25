from django.shortcuts import render
from .models import Product, SERVICE
from .serializers import ProductSerializer, ServiceSerializer
from rest_framework import generics
# Create your views here.


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ServiceView(generics.ListAPIView):
    queryset = SERVICE.objects.all()
    serializer_class = ServiceSerializer
