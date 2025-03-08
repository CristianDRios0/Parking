from django.contrib import admin
from .models import Tarifa

@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'vehiculo_tipo', 'monto', 'fecha_actualizacion')
    search_fields = ('tipo', 'vehiculo_tipo')
    list_filter = ('tipo', 'vehiculo_tipo', 'fecha_actualizacion')
    ordering = ('fecha_actualizacion',)
