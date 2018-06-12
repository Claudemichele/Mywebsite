from django.db import models
from django.utils import timezone


class Background(models.Model):
    text = models.TextField()
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


