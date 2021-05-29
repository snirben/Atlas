

from django import forms
from atlasapp.choices import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import User, Mission, Item, Complain, Message, Message_to_parents, Health
from django.forms import ModelForm, DateInput
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

class AddItemForm(forms.ModelForm):

    def init(self, *args, **kwargs):
        super(AddItemForm, self).init(*args, **kwargs)
        self.fields["image"].required=False
        self.fields["audio"].required=False

    class Meta:
        model = Item
        fields = ["image", "audio", "subject","gametype"]


class gameChoicesForm(forms.Form):
    gametype=forms.ChoiceField(choices = GAME_CHOICES, required=True)





class AddComplainForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(AddComplainForm, self).init(*args, **kwargs)

    class Meta:
        model = Complain
        fields = ["text", "done", "user","date"]


class AddMessageForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(AddMessageForm, self).init(*args, **kwargs)

    class Meta:
        model = Message
        fields = ['message','gan']


class AddMessageForm_to_parents(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(AddMessageForm_to_parents, self).init(*args, **kwargs)

    class Meta:
        model = Message_to_parents
        fields = ['message','gan']



class Healthform(forms.ModelForm):
    def init(self, *args, **kwargs):
        super(Healthform, self).init(*args, **kwargs)

    class Meta:
        model = Health
        fields = ['heat','cov19','simp','family','file']