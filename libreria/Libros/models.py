from django.db import models


class Locales(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=100)
    #logo = models.ImageField()
    horario = models.CharField(max_length=100)

class Editorial(models.Model):
    nombre = models.CharField(max_length=30)

class Libros(models.Model):
    
    