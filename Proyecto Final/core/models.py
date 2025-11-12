from django.db import models

# Create your models here.
# Clases Tablas SQL

class Users (models.Model):
    Name = models.CharField(max_length=100)
    id_users = models.CharField(max_length=10, unique=True)
    Password = models.CharField(max_length=10)



