from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(('title'), max_length=24)
    date_created = models.DateTimeField(('date created'), auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Task(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(('name'), max_length=24)
    description = models.CharField(('description'), max_length=150)
    date_created = models.DateTimeField(('date created'), auto_now_add=True)
    is_completed = models.BooleanField(('Completed'), default=False, blank=True)

    def __str__(self):
        return f'{self.name}'
