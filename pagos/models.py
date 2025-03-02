from django.db import models
from clientes.models import Cliente
from parqueos.models import Parqueo

class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    parqueo = models.ForeignKey(Parqueo, on_delete=models.CASCADE, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id} - ${self.monto}"
