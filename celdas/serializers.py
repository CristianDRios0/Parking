from rest_framework import serializers
from .models import Celda

class CeldaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celda
        fields = '__all__'