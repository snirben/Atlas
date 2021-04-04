from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import User
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

