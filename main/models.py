from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(('title'), max_length=30)
    date_created = models.DateTimeField(('date created'), auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    def is_new(self):
        date_now = timezone.now()
        difference = (date_now - self.date_created).total_seconds()

        if (difference / 60 / 60 / 24) < 1:
            return True


class Task(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(('name'), max_length=24)
    description = models.CharField(('description'), max_length=150)
    date_created = models.DateTimeField(('date created'), auto_now_add=True)
    is_completed = models.BooleanField(('Completed'), default=False, blank=True)

    def __str__(self):
        return f'{self.name}'
