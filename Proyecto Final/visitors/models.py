from django.db import models

# Create your models here.

class Visitor (models.Model):
    VISITOR_TYPE =(
        ('TEMP', 'Visitante Temporal'),
        ('PROV', 'Proveedor'),
        ('EMP', 'Empleado')
    )
    name = models.CharField(max_length=100)
    id_visitor = models.CharField(max_length=10, unique=True)
    visitor_type = models.CharField(max_length=5, choices=VISITOR_TYPE)
    motive = models.CharField(max_length=120)