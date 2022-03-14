from faulthandler import cancel_dump_traceback_later
from django.db import models

# Create your models here.
class Cerrajero(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    desempleado = models.BooleanField()
 
class Futbolista(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    club_futbol = models.CharField(max_length=40)


# o     
# class Profesional(models.Model):
#     nombre = models.CharField(max_length=20)
#     apellido = models.CharField(max_length=30)

# class Cerrajero(Profesional):
#     desempleado = models.BooleanField()
 
# class Futbolista(Profesional):
#     club_futbol = models.CharField(max_length=40)