from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
import random
from django.db.models import Sum,Avg
from atlasapp.forms import AddUserForm, AddMissionForm, AddItemForm, AddComplainForm, AddMessageForm
from atlasapp.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse



@login_required
def home(request):
    context = {}
    return render(request, 'atlasapp/home.html', context)


def registerpage(request):
    context = {}
    return render(request, 'atlasapp/register.html', context)


def loginpage(request):
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
    return render(request, 'atlasapp/login.html', context)


def SupervisorHome(request):
    missions = Mission.objects.all()
    gananot = User.objects.filter(role=1)
    context = {'missions': missions, 'gananot': gananot}
    return render(request, 'atlasapp/SupervisorHome.html', context)


def GannetHome(request):
    context = {}
    return render(request, 'atlasapp/GannetHome.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def missions_view(request):
    missions = Mission.objects.all()
    context = {'missions': missions}
    return render(request, 'atlasapp\manageMissions.html', context)


def delete_mission(request, part_id=None):
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
    context = {'missions': items}
    return render(request, 'atlasapp\gManageGames.html', context)


def delete_item(request, part_id=None):
    obj = Item.objects.get(id=part_id)
    obj.delete()
    return redirect('gManageGames')


def createItem(request):
    form = AddItemForm(request.POST, request.FILES)
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
    context = {'users': users}
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
    context = {'missions': missions}
    return render(request, 'atlasapp\gManageMissions.html', context)


def get_mission_done(request, part_id=None):
    obj = Mission.objects.get(id=part_id)
    obj.done = True
    obj.save()
    return redirect('gManageMissions')


@login_required
def childhome(request):
    context = {}
    return render(request, 'atlasapp/childhome.html', context)


@login_required
def studycategory(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'atlasapp/studycategory.html', context)


@login_required
def studysubcategory(request, part_id):
    subject = Subject.objects.get(id=part_id)
    SubSubjects = SubSubject.objects.filter(subject_id=subject.id)
    context = {'SubSubjects': SubSubjects}
    return render(request, 'atlasapp/studysubcategory.html', context)


@login_required
def pickgame(request, id):
    subsubject = SubSubject.objects.get(id=id)
    SubSubjects = SubSubject.objects.filter(name=subsubject.name)
    context = {'SubSubjects': SubSubjects}
    return render(request, 'atlasapp/pickgame.html', context)


@login_required
def memory_game(request, subsubject_id):
    items = Item.objects.filter(subject_id=subsubject_id)
    game = Game(user=request.user)
    game.save()
    context = {'items': items, 'game': game}
    return render(request, 'atlasapp/memory_game.html', context)


@login_required
def someInThePicture_view(request, subject_id):
    context = {'subject_id': subject_id}
    return render(request, 'atlasapp/someInThePicture.html', context)


@login_required
def someInThePictureGame(request, subject_id):
    items = Item.objects.filter(subject_id=subject_id)
    game = Game(user=request.user)
    game.save()
    context = {'items': items, 'game': game}
    return render(request, 'atlasapp/someInThePictureGame.html', context)


@login_required
def colorgame(request, subsubject_id):
    items = Item.objects.filter(subject_id=subsubject_id)
    game = Game(user=request.user)
    game.save()
    context = {'items': items, 'game': game}
    return render(request, 'atlasapp/colorgame.html', context)


def end_memory_game(request):
    game_id = request.GET.get('game_id')
    steps = request.GET.get('steps')
    game = get_object_or_404(Game, pk=game_id)
    game.steps = steps
    game.save()
    return JsonResponse(data={}, status=200)


def endsomeinthepicturegame(request):
    game_id = request.GET.get('game_id')
    steps = request.GET.get('steps')
    game = get_object_or_404(Game, pk=game_id)
    game.steps = steps
    game.save()
    return JsonResponse(data={}, status=200)


def end_color_game(request):
    game_id = request.GET.get('game_id')
    steps = request.GET.get('steps')
    game = get_object_or_404(Game, pk=game_id)
    game.steps = steps
    game.save()
    return JsonResponse(data={}, status=200)

@login_required
def sComplainpage_view(request):
    complains = Complain.objects.all()
    context = {'complains': complains}
    return render(request, 'atlasapp/sComplainpage.html', context)

def update_complain(request, part_id):
    complain = Complain.objects.get(id=part_id)
    complain.done = True
    complain.save()
    return redirect('sComplainpage')

def createcomplain(request):
    form = AddComplainForm(request.POST or None)
    user = Complain(user=request.user)
    if form.is_valid():
        form.save()
        return redirect('childhome')
    else:
        form = AddComplainForm()
    return render(request, 'atlasapp/addcomplain.html', {'form': form, 'user':user})

@login_required
def reports(request):
    user = User.objects.get(pk=request.user.id)
    users = User.objects.filter(gan_id=user.gan.id)
    data =[]
    for u in users:
        steps = Game.objects.filter(user=u).aggregate(total_steps=Avg('steps'))['total_steps']
        data.append({'name':u.name+''+u.lastname,'gan':u.gan.name,'games':len(Game.objects.filter(user=u)),'steps':round(steps,0),'level':round(steps,0)+1})
    return render(request, 'atlasapp/gannet_reports.html', {'data': data})


@login_required
def messages(request):
    messages = Message.objects.all()
    return render(request, 'atlasapp/supervisor_messages.html', {'messages': messages})

@login_required
def add_messages(request):
    form = AddMessageForm(request.POST)
    if form.is_valid():

        form.save()
        return redirect('messages')
    else:
        form = AddMessageForm()
    return render(request, 'atlasapp/add_message_supervisor.html', {'form': form})

def capsules_view(request):
    context = {}
    return render(request, 'atlasapp/create_capsules.html', context)