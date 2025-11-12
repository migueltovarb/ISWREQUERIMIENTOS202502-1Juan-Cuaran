from django.db import models

# Create your models here.

class vehiculos (models.Model):
    COLORLIST =(
        ('1', 'ROJO'),
        ('2', 'AZUL'),
        ('3', 'VERDE'),
    )
    placa = models.CharField(max_length=6)
    marca = models.CharField(max_length=10)
    color = models.CharField('color',max_length=1, choices=COLORLIST)
    modelo = models.IntegerField()

    
