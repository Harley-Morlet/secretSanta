from django.db import models
from django.utils import timezone

class Participant(models.Model):
    name = models.CharField(max_length=100, unique=True)
    assigned_name = models.CharField(
        max_length=100,
        default="Unassigned - Waiting for everyone to join"
    )
    password = models.CharField(max_length=128)
    signup_date = models.DateTimeField(default=timezone.now)
    gift_preference = models.CharField(max_length=255, blank=True, null=True)  # New field


    def __str__(self):
        return self.name