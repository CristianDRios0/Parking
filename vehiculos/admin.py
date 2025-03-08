from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente', 'placa')
    list_filter = ('cliente',)
    search_fields = ('placa', 'cliente__nombre')
    ordering = ('placa',)

    def get_cliente(self, obj):
        return obj.cliente.nombre if obj.cliente else "Sin cliente"
    get_cliente.short_description = 'Cliente'
