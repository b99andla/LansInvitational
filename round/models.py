from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Round(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Score(models.Model):
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE
    )


class ScoreLine(models.Model):
    strokes = models.IntegerField(null=True)
    points = models.IntegerField(null=True)
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
