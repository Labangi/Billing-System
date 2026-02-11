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

def insert(request):    
    return render(request,'insert.html')

def add_customer(request):
    u=user()
    u.username=request.GET['username']
    u.email=request.GET['email']
    u.pwd=request.GET['password']
    u.role=request.GET['role']
    u.save()
    return redirect('../')

def show(request):
    users = user.objects.all()
    return render(request, "show.html", {"users": users})

def update_role(request, id):
    if request.method == "POST":
        user = user.objects.get(id=id)
        user.role = request.POST.get("role")
        user.save()
    return redirect("../show.html")
def about_us(request):
    return render(request,"about_us.html")
def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")

def admin_dashboard(request):
    return render(request, 'admin.html')

def training_bills(request):
    return render(request, 'training_bills.html')
