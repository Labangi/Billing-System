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
    pass
