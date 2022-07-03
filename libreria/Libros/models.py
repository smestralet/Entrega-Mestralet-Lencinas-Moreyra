from django.db import models


class Locales(models.Model):
    nombre = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=100)
    #logo = models.ImageField()
    horario = models.CharField(max_length=100)

class Editorial(models.Model):
    nombre = models.CharField(max_length=30)
    link_editorial = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='imgs/')

    def __str__(self):
        return self.nombre


class Libros(models.Model):
    name = models.CharField(max_length=255)
    autor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    precio = models.FloatField()
    ISBN = models.CharField(max_length=20, unique=True)
    stock = models.BooleanField(default=True, null=True)
    fecha = models.DateTimeField()
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

