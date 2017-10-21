from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
# Create your views here.
def index(request):
    context = {
        "users":User.objects.all()

    }
    return render(request, "users/index.html",context)

def admin(request):
    context = {
        "users":User.objects.all()

    }
    return render(request, "users/admin.html",context)


def show(request,id):
    
    return render(request, "users/show.html",{"users":User.objects.get(id=id)})


def edit(request,id):
    return render(request, "users/edit.html",{"users":User.objects.get(id=id)})

def processedit(request,id):
    
    entry = User.objects.get(id=id)
    entry.first_name = request.POST['first_name']
    entry.last_name =  request.POST['last_name']
    entry.email = request.POST['email']
    entry.save()
    
    return redirect("/dashboard/users/admin")

def add(request):
    
    return render(request,"users/add.html")

def new(request):
    
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/dashboard/users/")

def delete(request,id):
    
    u = User.objects.get(id=id)
    u.delete() 
    return redirect("/dashboard/users")