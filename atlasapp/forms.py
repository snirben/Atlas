from django import forms
from atlasapp.choices import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import User, Mission
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView


class AddUserForm(ModelForm): #linoy add for user story 3
    password = forms.CharField(widget=forms.PasswordInput)

    def _init_(self, *args, **kwargs):
        super(AddUserForm, self)._init_(*args, **kwargs)
        self.fields['lastname'].widget.attrs['class'] = "form-control"

    class Meta:
        model = User
        fields = ["username", "password", "name", "lastname","gan","phone", "email", "mevodad", "covid", "role"]


class AddMissionForm(forms.ModelForm):
    # mission = forms.CharField(initial='class')

    def init(self, *args, **kwargs):
        super(AddMissionForm, self).init(*args, **kwargs)

    class Meta:
        model = Mission
        fields = ["text", "done", "gannet"]


class gameChoicesForm(forms.Form):
    gametype=forms.ChoiceField(choices = GAME_CHOICES, required=True)