from django.db import models

# Create your models here.
class Player_Info(models.Model):
    player_name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    age = models.IntegerField()
    matches_played = models.IntegerField()
    runs_scored = models.IntegerField()
    wickets_taken = models.IntegerField()

    def __str__(self):
        return self.player_name
    
class Supporting_Staff(models.Model):
    Staff_name = models.CharField(max_length=100)
    S_Position = models.CharField(max_length=100)
    age = models.IntegerField()
    experience_years = models.IntegerField()
    
