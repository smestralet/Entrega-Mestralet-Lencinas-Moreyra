from django.db import models


class Locales(models.Model):
    nombre_local = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=100)
    #logo = models.ImageField()
    horario = models.CharField(max_length=100)

class Editorial(models.Model):
    nombre_editorial = models.CharField(max_length=30)

class Libros(models.Model):
    nombre_libro = models.CharField(max_length=255)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.FloatField()
    ISBN = models.CharField(max_length=20,Uniques=True)
    stock = models.BooleanField(default=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

