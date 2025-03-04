from django.db import models
from vehiculos.models import Vehiculo
from celdas.models import Celda 
from tarifas.models import Tarifa

class Parqueo(models.Model):
    ESTADO_PARQUEO = [
        ('activo', 'Activo'),
        ('finalizado', 'Finalizado'),
    ]
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    celda = models.ForeignKey(Celda, on_delete=models.CASCADE)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.RESTRICT)
    fecha_entrada = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_PARQUEO, default='activo')
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'parqueos'

    def __str__(self):
        return f"Parqueo {self.id} - {self.vehiculo.placa} - {self.estado}"
