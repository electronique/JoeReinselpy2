from django.shortcuts import render, HttpResponse, redirect

import bcrypt
from django.contrib import messages

from models import *

# Create your views here.
def index(request):

    return render(request,'loginreg/index.html')

def create(request):
    
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            print 'need more information'
            
            return redirect('/loginreg')
    else:
        request.session['first_name']=request.POST['first_name']
        request.session['last_name']=request.POST['last_name']
        request.session['email']=request.POST['email']
        password = request.POST['password']
        pw_hash =  bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print pw_hash
       
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'], password= pw_hash)

    return redirect('/loginreg')

def login(request):
    try:
        request.POST['loginemail']
        request.POST['password']
    except:
        pass
    request.session['loginemail'] = request.POST['loginemail']
    email = request.session['loginemail']
    pwd = request.POST['password']

    emailsearch = User.objects.filter(email=email)[0].email
    #still need to work on email validation
    passwordsearch = User.objects.get(password=pwd)[0].password
    print passwordsearch
    print emailsearch
    # database query is incorrect
    print request.session['loginemail']
    if request.session['loginemail'] == emailsearch:
        print "success"
        return render(request,'loginreg/success.html')
        
    else:
        print "error"
        return redirect('/loginreg') 