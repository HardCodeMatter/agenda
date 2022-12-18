from django.contrib import admin
from .models import Profile, Task


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'user')
    fields = ('title', 'date_created', 'user')
    readonly_fields = ('date_created',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'date_created', 'is_completed')
    fields = ('name', 'description', 'profile', 'is_completed', 'date_created')
    readonly_fields = ('date_created',)
