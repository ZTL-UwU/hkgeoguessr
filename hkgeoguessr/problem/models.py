from email.policy import default
from django.db import models

# Create your models here.


class Problem(models.Model):
    pid = models.IntegerField(unique=True, default=0)
    video_link = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=1500)

    start_geo = models.IntegerField(default=0)
    end_geo = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pid)
