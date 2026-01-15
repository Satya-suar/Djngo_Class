from django.db import models

# Create your models here.
class Shirt(models.Model):
    Brand = models.CharField(max_length=100)
    Price = models.FloatField()
    Color = models.CharField(max_length=10)
    