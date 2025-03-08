from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'identificacion', 'tipo_plan', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre', 'identificacion')
    list_filter = ('tipo_plan',)
