from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'user')
    fields = ('title', 'date_created', 'user')
