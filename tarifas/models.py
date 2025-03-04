from django.db import models

class Tarifa(models.Model):
    TIPO_TARIFA = [
        ('hora', 'Hora'),
        ('mensual', 'Mensual'),
    ]
    TIPO_VEHICULO = [
        ('automovil', 'Automovil'),
        ('moto', 'Moto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_TARIFA)
    vehiculo_tipo = models.CharField(max_length=10, choices=TIPO_VEHICULO)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tarifas'

    def __str__(self):
        return f"{self.tipo} - {self.vehiculo_tipo} - ${self.monto}"
