from django import forms
from .models import Player
from django.contrib.auth.forms import AuthenticationForm

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'age', 'team', 'position']

class CoachLoginForm(AuthenticationForm):
    pass

class PlayerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'team', 'position', 'age']  # Add fields relevant to the Player model