from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from movies.models import Character


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class CharacterForm(forms.ModelForm):
    def validate_unique(self):
        pass

    class Meta:
        model = Character
        fields = ('person', 'name')
