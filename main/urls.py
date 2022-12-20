from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('profile/', views.profile_list, name='profile_list'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile/<int:id>/', views.profile_view, name='profile_view'),
    path('profile/<int:id>/create/', views.task_create, name='task_create'),
]
