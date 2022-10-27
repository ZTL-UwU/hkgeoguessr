from email.policy import default
from xml.etree.ElementInclude import default_loader
from django.db import models


class Money(models.Model):
    pid = models.IntegerField(unique=True)
    video_link = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=1500)

    start_geo = models.IntegerField(default=0)
    end_geo = models.IntegerField(default=0)

    answered = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['pid']),
            models.Index(fields=['rating']),
        ]

    def __str__(self):
        return str(self.pid)
