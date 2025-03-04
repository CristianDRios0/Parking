from django.db import models
from clientes.models import Cliente

class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    placa = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'vehiculos'

    def __str__(self):
        return self.placa
