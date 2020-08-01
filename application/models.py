from django.db import models
import datetime
from django.contrib.auth.models import User, auth
# Create your models here.


class league(models.Model):
    league_name = models.CharField(max_length=255, unique=True)
    league_logo = models.ImageField(upload_to='league_logos')
    league_address = models.CharField(max_length=255)
    league_number = models.CharField(max_length=25)
    league_more_info = models.TextField(default="None")
    added_date = models.DateTimeField(default=datetime.datetime.now)

    def make_url_name(self):
        self.url_name = self.league_name.split(" ")
        self.url_name = "-".join(self.url_name)

    def __str__(self):
        return self.league_name



class division(models.Model):
    division_name = models.CharField(max_length=255)
    parent_league = models.ForeignKey(league, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "{}  -  ( {} )".format(self.division_name, self.parent_league.league_name)


class team(models.Model):
    team_logo = models.ImageField(upload_to='team_logos')
    team_name = models.CharField(max_length=150)
    team_captain = models.ForeignKey(User, on_delete=models.CASCADE)
    representative_name = models.CharField(max_length=150)
    representative_pic = models.ImageField(upload_to='representatives')
    coach_name = models.CharField(max_length=150)
    coach_pic = models.ImageField(upload_to='coaches')
    date_created = models.DateTimeField(default=datetime.datetime.now)
    
    def get_players(self):
        if player.objects.filter(parent_team = self).exists():
            self.all_players = player.objects.filter(parent_team = self)
        else:
            self.all_players = None

class player(models.Model):
    parent_team = models.ForeignKey(team, on_delete=models.CASCADE)
    player_img = models.ImageField(upload_to='player_pics')
    player_name = models.CharField(max_length=150)
    player_phone = models.CharField(max_length=150)
    player_dob = models.DateField()

class profile_pics(models.Model):
    id = models.IntegerField(primary_key=True)
    user_img = models.ImageField(upload_to='profilePics')

    def __str__(self):
        thisUSER = User.objects.get(id=self.id)
        return thisUSER.username

