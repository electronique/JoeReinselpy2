from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    print "test index"
    return render(request,'randomword/index.html')

def random(request):
    try:
        request.session['counter']
    except(KeyError):
        request.session['counter']=1

    request.session['counter']+=1
    context = {
        'randomwords': get_random_string(length=32),
        'counting': request.session['counter']
    }
    
    
    return render(request,'randomword/index.html',context)
