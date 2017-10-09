from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    response = "this is a placeholder to display all the surveys created"
    return HttpResponse(response)
def new(request):
    response = "this is a placeholder to display all new surveys created"
    return HttpResponse(response)