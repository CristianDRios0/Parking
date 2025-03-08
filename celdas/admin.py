from django.contrib import admin
from .models import Celda

@admin.register(Celda)
class CeldaAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'tipo', 'estado')
    search_fields = ('codigo',)
    list_filter = ('tipo', 'estado')

