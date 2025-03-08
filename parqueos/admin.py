from django.contrib import admin
from .models import Parqueo

@admin.register(Parqueo)
class ParqueoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_vehiculo', 'celda', 'tarifa', 'fecha_entrada', 'fecha_salida', 'estado', 'total_pagado')
    search_fields = ('vehiculo__placa',)
    list_filter = ('estado', 'fecha_entrada', 'fecha_salida',)

    def get_vehiculo(self, obj):
        return obj.vehiculo.placa
    
    get_vehiculo.short_description = 'Vehículo'
