from django import forms
from .models import Profile, Task


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('title',)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'description', 'is_completed')
