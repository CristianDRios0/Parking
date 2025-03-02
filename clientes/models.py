from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_plan = models.CharField(max_length=10, choices=[('mensual', 'Mensual'), ('ocasional', 'Ocasional')], default= 'ocasional')
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'clientes' # Nombre de la tabla en la base de datos se una para que django no cree una nueva tabla

    def __str__(self):
        return f"(self.user.username - self.tipo_plan)"

