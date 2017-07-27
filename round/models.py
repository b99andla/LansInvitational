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

    def save(self, **kwargs):
        is_new = self.id is None
        super(Team, self).save()
        if is_new:
            Score.objects.create(team=self)


class Score(models.Model):
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} score'.format(self.team)

    def save(self, **kwargs):
        is_new = self.id is None
        super(Score, self).save()
        if is_new:
            for x in range(1, 19):
                ScoreLine.objects.create(score=self, hole=x)


class ScoreLine(models.Model):
    hole = models.IntegerField(
        "Hål",
        null=False,
    )
    strokes = models.IntegerField(
        "Antal slag",
        null=True,
        blank=True)
    score = models.ForeignKey(Score)
