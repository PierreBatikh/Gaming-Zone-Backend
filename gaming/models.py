from datetime import timezone
import uuid
from django.db import models

# Create your models here.

# class Newbie(models.Model):
#     name = models.CharField(max_length=200)
#     age = models.IntegerField()
#     platform = models.CharField(max_length=255)
#     favourite_game = models.CharField(max_length=255)
#     genres = models.JSONField() # search for this 
# this was one way, but I am doing the following instead:


class Submitter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    

class Pro(models.Model):
    platform = models.CharField(max_length=32)
    fav_game = models.CharField(max_length=64)
    genre = models.TextField()
    game_art_style = models.CharField(max_length=32)
    clash_royal = models.TextField()
    hollow_knight = models.TextField()
    rdr2 = models.TextField()
    submitter = models.ForeignKey(Submitter, on_delete=models.CASCADE)
    

class Newbie(models.Model):
    platform = models.CharField(max_length=32)
    fav_game = models.CharField(max_length=64)
    genre = models.CharField(max_length=32)
    submitter = models.ForeignKey(Submitter, on_delete=models.CASCADE)
    


# I guess this should go to forms.py