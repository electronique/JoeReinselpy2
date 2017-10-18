from django.shortcuts import render, HttpResponse, redirect

from models import *
# Create your views here.
def index(request):
    try:
        course.objects.all()
    except:
        pass

    return render(request, "courses/index.html",{"courses": course.objects.all()})

def add(request):
        course.objects.create(name=request.POST['name'],description=request.POST['description'])
        
        return redirect('/courses')
def remove(request,id):
     course.objects.get(id=id)
     return render(request,"courses/coursealert.html", {"courses":course.objects.get(id=id)})
def delete(request,id):

    c = course.objects.get(id=id)
    c.delete()
    return redirect("/courses")