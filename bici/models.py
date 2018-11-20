from django.db import models

# Create your models here.


class Bici(models.Model):
	codigo = models.CharField(max_length=50)
	estacionamiento = models.CharField(max_length=10)
	direccion = models.CharField(max_length=50)
	disponible = models.BooleanField()

