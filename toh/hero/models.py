from django.db import models
from django.db.models.fields import related

class Hero(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=120)

    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set',
    )       
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )

    def __str__(self):
        return self.name