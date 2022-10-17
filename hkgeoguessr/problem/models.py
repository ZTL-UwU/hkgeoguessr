from django.db import models


class Problem(models.Model):
    pid = models.IntegerField(unique=True)
    video_link = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=1500)

    start_geo = models.IntegerField(default=0)
    end_geo = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['pid']),
            models.Index(fields=['rating']),
        ]

    def __str__(self):
        return str(self.pid)
