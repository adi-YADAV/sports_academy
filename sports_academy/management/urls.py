from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.coach_login, name='coach_login'),
    path('logout/', views.coach_logout, name='coach_logout'),
    path('register-player/', views.player_registration, name='player_registration'),
    path('update-player/<int:player_id>/', views.update_player, name='update_player'),
    path('players/', views.player_list, name='player_list'),
]


