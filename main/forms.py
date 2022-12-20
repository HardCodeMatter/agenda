from django import forms
from .models import Task


class ProfileForm(forms.Form):
    title = forms.CharField(max_length=24)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'is_completed')
