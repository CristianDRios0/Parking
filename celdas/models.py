from django.db import models

class Celda(models.Model):
    TIPO_VEHICULO = [
        ('Automovil', 'automovil'),
        ('Moto', 'moto'),
    ]
    ESTADO_CELDA = [
        ('Libre', 'libre'),
        ('Ocupado', 'ocupado'),
        ('Reservado', 'reservado'),
    ]
    codigo = models.CharField(max_length=10, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPO_VEHICULO)
    estado = models.CharField(max_length=10, choices=ESTADO_CELDA, default='Libre')

    class Meta:
        db_table = 'celdas'

    def __str__(self):
        return f"Celda {self.codigo} - {self.tipo} - {self.estado}"
