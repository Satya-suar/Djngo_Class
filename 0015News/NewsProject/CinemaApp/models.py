from django.db import models

# Create your models here.
class Writer_Info(models.Model):
    writer_name = models.CharField(max_length=100)
    age = models.IntegerField() 
    experience_years = models.IntegerField()
    articles_written = models.IntegerField()
    awards_won = models.IntegerField()
    
    
class Actor_Actress_Info(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies_done = models.IntegerField()
    awards_won = models.IntegerField()
    debut_year = models.IntegerField()

class Director_Info(models.Model):
    director_name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies_directed = models.IntegerField()
    awards_won = models.IntegerField()
    debut_year = models.IntegerField()