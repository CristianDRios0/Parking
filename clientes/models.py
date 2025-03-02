from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    TIPO_PLAN = [
        ('Mensual', 'mensual'),
        ('Ocasional', 'ocasional'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_plan = models.CharField(max_length=10, choices=TIPO_PLAN)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.tipo_plan}"
