from rest_framework import serializers
from . import models


class LaptopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Laptops
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ['name']