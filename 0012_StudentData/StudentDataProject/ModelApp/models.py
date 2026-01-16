from django.db import models

# Create your models here.
class StudentData(models.Model):
    Regd=models.CharField(max_length=30)
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    