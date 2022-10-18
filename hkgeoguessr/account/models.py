from email.policy import default
from enum import unique
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    uid = models.IntegerField(unique=True)
    rating = models.IntegerField(default=1500)
    avatar_url = models.TextField(blank=True, null=True)

    first_name = None  # delete unused field
    last_name = None  # delete unused field

    def __str__(self):
        return self.username
