from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(('title'), max_length=24)
    date_created = models.DateTimeField(('date created'), auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
