from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


class Round(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Runda"


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

    class Meta:
        verbose_name = "Lag"


class Score(models.Model):
    team = models.OneToOneField(
        Team,
        on_delete=models.CASCADE
    )

    @property
    def total_strokes(self):
        strokes = self.scoreline_set.aggregate(Sum('strokes'))
        print(strokes['strokes__sum'])
        if strokes['strokes__sum'] is not None:
            return strokes['strokes__sum']
        else:
            return '-'

    @property
    def on_hole(self):
        hole = self.scoreline_set.exclude(strokes__isnull=True).count()
        if hole == 0:
            return 'Har inte startat än'
        if hole == 18:
            return 'har gått klart'
        else:
            return hole + 1

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
