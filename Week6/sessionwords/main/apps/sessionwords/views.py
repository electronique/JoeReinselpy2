from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "sessionwords/index.html")

def process(request):
    if request.method == "POST":
        # multiple words => need array . Be care of adding to an array
        temparr = request.sesson["words"]
        temparr.append("word")
        request.session["words"] = temparr
        request.session['words']=request.POST['words']
        print request.session['words']
        return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')