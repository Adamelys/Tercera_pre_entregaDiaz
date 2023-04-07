from django.db import models

# Create your models here.
class Chat(models.Model):
    fecha_hora      = models.DateField()
    usuario         = models.CharField(max_length=30)
    id_mensaje      = models.IntegerField()
    conversacion    = models.CharField(max_length=250)
