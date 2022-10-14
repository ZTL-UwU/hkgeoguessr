from email.policy import default
from msilib.schema import Class
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Account(AbstractUser):
    rating = models.IntegerField(default = 1500)
    banned = models.BooleanField(default = False)
    potential_cheats = models.IntegerField(default = 0)