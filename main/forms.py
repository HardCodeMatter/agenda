from django import forms
from .models import Task


class ProfileForm(forms.Form):
    title = forms.CharField(max_length=24)


class TaskForm(forms.Form):
    name = forms.CharField(max_length=30)
    description = forms.CharField(max_length=150)
