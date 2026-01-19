from django.db import models

# Create your models here.
class Mp_Info(models.Model):
    mp_name = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    age = models.IntegerField()
    terms_served = models.IntegerField()
    bills_passed = models.IntegerField()
    party_affiliation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.mp_name




class MLA_Info(models.Model):
    mla_name = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    age = models.IntegerField()
    terms_served = models.IntegerField()
    development_projects = models.IntegerField()
    party_affiliation = models.CharField(max_length=100)
    
    def __str__(self):
        return self.mla_name
