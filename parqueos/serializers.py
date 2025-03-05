from rest_framework import serializers
from .models import Parqueo
from celdas.models import Celda
from datetime import datetime

class ParqueoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parqueo
        fields = '__all__'

        def update(self, instance, validated_data):
        
            if 'fecha_salida' in validated_data and validated_data['fecha_salida']:
                instance.fecha_salida = validated_data['fecha_salida']
                instance.estado = 'finalizado'
                instance.celda.estado = 'Libre'  
                instance.celda.save()

                duracion_horas = (instance.fecha_salida - instance.fecha_entrada).total_seconds() / 3600
                instance.total_pagado = round(duracion_horas * instance.tarifa.monto, 2)

            return super().update(instance, validated_data)