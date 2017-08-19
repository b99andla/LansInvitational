from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handicap = models.FloatField(blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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

    def hancicap(self):
        players = User.objects.filter(team=self)
        if(len(players) == 1):
            return players[0].handicap
        if(len(players) == 2):
            return players

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
        if strokes['strokes__sum'] is not None:
            return strokes['strokes__sum']
        else:
            return '-'

    @property
    def total_points(self):
        points = self.scoreline_set.aggregate(Sum('points'))
        print(points)
        if points['points__sum'] is not None:
            return points['points__sum']
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
    points = models.IntegerField(
        "Antal poäng",
        null=True,
        blank=True)
    score = models.ForeignKey(Score)
