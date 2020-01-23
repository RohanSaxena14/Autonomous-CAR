from django.urls import path
from . import views

urlpatterns = [
    path('home', views.stop, name='stop'),
    path('command_up', views.command_up, name='command_up'),
    path('command_down', views.command_down, name='command_down'),
    path('command_right', views.command_right, name='command_right'),
    path('command_left', views.command_left, name='command_left')
]
