from django.db import models

# Create your models here.
class Familiares(models.Model):

    Parentesco = models.CharField(max_length=40)
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    FechaDeNacimiento = models.DateField()
