from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.camada}, Camada: {self.camada}"

class Estudiantes (models.Model):
    nombre   = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email    = models.EmailField

class Profesor (models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"Profesor: {self.nombre}, Apellido: {self.apellido}"

class Entregable(models.Model)
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField

