from django.db import models
from django.utils import timezone

# Create your models here.
class AccessPoint(models.Model):
    name = models.CharField(max_length=80)

class AccessEvent(models.Model):

    STATUS_ACCESS = [
        ('ENTRY', 'Entrada'),
        ('EXIT', 'Salida')
    ]

    timestamp = models.DateTimeField(default=timezone.now)
    access_point = models.ForeignKey(AccessPoint, on_delete=models.CASCADE)
    credential = models.CharField(max_length=6)
    status = models.CharField(max_length=5, choices=STATUS_ACCESS)
