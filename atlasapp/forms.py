from django import forms
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from .models import User
from .models import Mission

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import UpdateView



class AddMissionForm(forms.ModelForm):
    # mission = forms.CharField(initial='class')

    def init(self, *args, **kwargs):
        super(AddMissionForm, self).init(*args, **kwargs)

    class Meta:
        model = Mission
        fields = ["text", "done", "gannet"]