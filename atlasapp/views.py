from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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