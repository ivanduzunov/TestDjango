from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    sport = models.TextField(max_length=100, blank=False)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.user.first_name + self.user.last_name
