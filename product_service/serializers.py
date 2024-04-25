from rest_framework import serializers
from .models import Product, SERVICE


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['NAME', 'SLUG', 'ICON', 'SHORT_DESCRIPTION']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SERVICE
        fields = ['NAME', 'SLUG', 'ICON', 'IMAGE', 'SHORT_DESCRIPTION']
