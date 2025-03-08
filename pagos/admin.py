from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'parqueo', 'monto')
    list_filter = ('cliente',)
    search_fields = ('cliente__nombre',)
 
