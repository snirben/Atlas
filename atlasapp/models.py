from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    #define roles
    ROLE = ((0, "Supervisor"),(1,"Gannet"),(2,"Child"))

    role = models.PositiveSmallIntegerField(choices=ROLE,default=2)
    mevodad = models.BooleanField(default=False)
    covid= models.BooleanField(default=False)
    name = models.CharField(max_length=50,null=False)
    lastname = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=50,null=False)