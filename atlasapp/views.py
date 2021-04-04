from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models

from atlasapp.forms import AddUserForm
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
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(
                request, messages.ERROR, "שם משתמש או סיסמא לא נכונים"
            )
    context = {}
    return render(request,'atlasapp/login.html',context)

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

def bidudim(request):
    gans = Gan.objects.all()
    context = {'gans': gans}
    return render(request, 'atlasapp/bidudim.html', context)

def gManageUsers(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'atlasapp/gManageUsers.html', context)