from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models

from atlasapp.forms import AddUserForm, AddMissionForm, AddItemForm
from atlasapp.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse


@login_required
def home (request):
    context = {}
    return render(request, 'atlasapp/home.html', context)

def registerpage (request):
    context={}
    return render(request,'atlasapp/register.html',context)

def loginpage (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user.role == 0:
            login(request, user)
            return redirect('SupervisorHome')
        elif user.role == 1:
            login(request, user)
            return redirect('GannetHome')
        elif user.role == 2:
            login(request, user)
            return redirect('childhome')
        elif user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(
                request, messages.ERROR, "שם משתמש או סיסמא לא נכונים"
            )
    context = {}
    return render(request,'atlasapp/login.html',context)

def SupervisorHome (request):
    missions = Mission.objects.all()
    context = {'missions': missions}
    return render(request, 'atlasapp/SupervisorHome.html', context)

def GannetHome (request):
    context = {}
    return render(request, 'atlasapp/GannetHome.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def missions_view(request):
    missions = Mission.objects.all()
    context = {'missions' : missions}
    return render(request, 'atlasapp\manageMissions.html',context)

def delete_mission(request, part_id = None):
    obj = Mission.objects.get(id=part_id)
    obj.delete()
    return redirect('manageMissions')

def createMission(request):
    form = AddMissionForm(request.POST or None)
    if form.is_valid():

        form.save()
        return redirect('manageMissions')
    else:
        form = AddMissionForm()
    return render(request, 'atlasapp/addMissions.html', {'form': form})

def games_view(request):
    items = Item.objects.all()
    context = {'missions' : items}
    return render(request, 'atlasapp\gManageGames.html',context)

def delete_item(request, part_id = None):
    obj = Item.objects.get(id=part_id)
    obj.delete()
    return redirect('gManageGames')

def createItem(request):
    form = AddItemForm(request.POST, request.FILES)
    print(request)
    if form.is_valid():

        form.save()
        return redirect('gManageGames')
    else:
        form = AddItemForm()
    return render(request, 'atlasapp/gAddItem.html', {'form': form})


def sManageUsers(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'atlasapp/sManageUsers.html', context)


def delete_user(request, part_id=None):
    obj = User.objects.get(id=part_id)
    obj.delete()
    return redirect('sManageUsers')


def createUser(request):
    form = AddUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sManageUsers')
    else:
        form = AddUserForm()
    return render(request, 'atlasapp/sAddUser.html', {'form': form})


@login_required
def edituser(request, id):
    obj = get_object_or_404(User, id=id)
    form = AddUserForm(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form': form}
        return render(request, 'atlasapp/sEditUser.html', context)

    else:
        context = {'form': form}
        return render(request, 'atlasapp/sEditUser.html', context)

def editItem(request, id):
    obj = get_object_or_404(Item, id=id)
    form = AddItemForm(request.POST, request.FILES, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form': form}
        return redirect('gManageGames')

    else:
        context = {'form': form}
        return render(request, 'atlasapp/gEditItem.html', context)


def bidudim(request):
    gans = Gan.objects.all()
    context = {'gans': gans}
    return render(request, 'atlasapp/bidudim.html', context)

def gManageUsers(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'atlasapp/gManageUsers.html', context)

def create_child(request):
    form = AddUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gManageUsers')
    else:
        form = AddUserForm()
    return render(request, 'atlasapp/gAddUser.html', {'form': form})

def delete_child(request, part_id=None):
    obj = User.objects.get(id=part_id)
    obj.delete()
    return redirect('gManageUsers')

@login_required
def edit_child(request, id):
    obj = get_object_or_404(User, id=id)
    form = AddUserForm(request.POST or None, instance=obj)
    context = {'form': form}

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {'form': form}
        return render(request, 'atlasapp/gEditUser.html', context)

    else:
        context = {'form': form}
        return render(request, 'atlasapp/gEditUser.html', context)

def missions_view_gannet(request):
    missions = Mission.objects.all()
    context = {'missions' : missions}
    return render(request, 'atlasapp\gManageMissions.html',context)


def get_mission_done(request, part_id = None):
    obj = Mission.objects.get(id=part_id)
    obj.done = True
    obj.save()
    return redirect('gManageMissions')

@login_required
def childhome (request):
    context = {}
    return render(request, 'atlasapp/childhome.html', context)

@login_required
def studycategory(request):
    subjects = Subject.objects.all()
    context = {'subjects':subjects}
    return render(request, 'atlasapp/studycategory.html', context)

@login_required
def studysubcategory(request, part_id):
    subject = Subject.objects.get(id=part_id)
    SubSubjects = SubSubject.objects.filter(subject_id = subject.id)
    context = {'SubSubjects':SubSubjects}
    return render(request, 'atlasapp/studysubcategory.html', context)

@login_required
def pickgame(request, id):
    subsubject = SubSubject.objects.get(id=id)
    SubSubjects = SubSubject.objects.filter(name = subsubject.name)
    context = {'SubSubjects':SubSubjects}
    return render(request, 'atlasapp/pickgame.html', context)

@login_required
def game(request):
    context = {}
    return render(request, 'atlasapp/game.html', context)
