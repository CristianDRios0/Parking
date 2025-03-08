from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    TIPO_PLAN = [
        ('mensual', 'Mensual'),
        ('ocasional', 'Ocasional'),
    ]
    nombre = models.CharField(max_length=255)
    identificacion = models.CharField(max_length=20, unique=True)
    tipo_plan = models.CharField(max_length=10, choices=TIPO_PLAN)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return f"{self.user.username} - {self.tipo_plan}"
