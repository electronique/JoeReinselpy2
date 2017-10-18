from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *
# Create your views here.
def index(request):
    context = {
        "users":User.objects.all()

    }
    return render(request, "semi_restful/index.html",context)


def show(request,id):
    
    return render(request, "semi_restful/show.html",{"users":User.objects.get(id=id)})


def edit(request,id):
    return render(request, "semi_restful/edit.html",{"users":User.objects.get(id=id)})

def processedit(request,id):
    
    entry = User.objects.get(id=id)
    entry.first_name = request.POST['first_name']
    entry.last_name =  request.POST['last_name']
    entry.email = request.POST['email']
    entry.save()
    
    return redirect("/semi_restful")

def add(request):
    
    return render(request,"semi_restful/add.html")

def new(request):
    
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'])
    return redirect("/semi_restful")

def delete(request,id):
    
    u = User.objects.get(id=id)
    u.delete() 
    return redirect("/semi_restful")