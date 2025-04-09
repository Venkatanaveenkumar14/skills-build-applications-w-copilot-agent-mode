from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class Activity(models.Model):
    activity_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=50, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    workout_id = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()