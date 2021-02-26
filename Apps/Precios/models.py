from django.db import models

# Create your models here.
class PreciosBtc(models.Model):
    fecha=models.DateTimeField()
    precioMax=models.FloatField()
    precioMin=models.FloatField()




