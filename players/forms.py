from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Player

class PlayerSingUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    date_born = forms.DateField(widget=forms.SelectDateWidget(years=range(1980,2024)))
    position = forms.ChoiceField(choices=Player.positions)
    dominant_leg = forms.ChoiceField(choices=Player.leg)
    specialty = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_born', 'position', 'dominant_leg', 'specialty', 'password1', 'password2')

class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'date_born', 'position', 'dominant_leg', 'specialty']

    