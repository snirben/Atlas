from django.contrib.auth.models import AbstractUser
from django.db import models
from atlasapp.choices import *


class Gan(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return '{}'.format(self.name)


class User(AbstractUser):
    # define roles
    ROLE = ((0, "Supervisor"), (1, "Gannet"), (2, "Child"))

    role = models.PositiveSmallIntegerField(choices=ROLE, default=2)
    mevodad = models.BooleanField(default=False)
    covid = models.BooleanField(default=False)
    name = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    phone = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    gan = models.ForeignKey(Gan, on_delete=models.CASCADE, null=True, blank=True)


class Mission(models.Model):
    text = models.TextField(max_length=3000, null=False)
    done = models.BooleanField(default=False)
    gannet = models.ForeignKey(Gan, on_delete=models.CASCADE)


class Subject(models.Model):
    gamesubject = models.CharField(max_length=50, null=False)

    def __str__(self):
        return '{}'.format(self.gamesubject)

class SubSubject(models.Model):
    subsubject = models.CharField(max_length=50, null=False);
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE);
    gametype = models.CharField(choices=GAME_CHOICES, max_length=30, default=1)



class Item(models.Model):
    image = models.ImageField(upload_to="image")
    audio = models.FileField(upload_to="audio")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    gametype = models.CharField(choices=COLOR_CHOICES, max_length=30 ,default=9)
