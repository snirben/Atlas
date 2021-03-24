from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
    return HttpResponse('home page')

def register (request):
    context={}
    return render(request,'atlasapp/register.html',context)

def login (request):
    context = {}
    return render(request,'atlasapp/register.html',context)