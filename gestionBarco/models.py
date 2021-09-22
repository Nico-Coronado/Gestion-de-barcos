from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

class Barco(models.Model):
    nombre = models.CharField(max_length=100)
    embarque = models.DateField()
    desembarque = models.DateField()

    def __str__(self):
        return self.nombre

class Tripulante(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50, choices=(("1","Grupo 1"),("2","Grupo 2")))
    barco = models.ForeignKey(Barco, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre