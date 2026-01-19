from django.db import models

# Create your models here.
class  Electronics(models.Model):
    PName = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Price = models.IntegerField()
    
    def __str__(self):
        return self.Brand
