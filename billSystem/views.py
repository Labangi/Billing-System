from django.shortcuts import render,redirect
from django.http import HttpResponse
from billSystem.models import *
import os
import  requests


# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginn(request):
    
    username=request.GET['a1']
    pwd=request.GET['a2']
    if user.objects.filter(username=username,pwd=pwd):
        u=user.objects.filter(username=username,pwd=pwd).first()
        x={'username':u.username,'pwd':u.pwd}
        request.session['aec']=x
        return render(request,'admin.html')

    else:
        return render(request,'index.html')

def logout(request):
    try:
        del request.session['aec']
        return render(request,'index.html')
    except KeyError:
        pass
