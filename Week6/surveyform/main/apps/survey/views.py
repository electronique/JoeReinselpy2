from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,"survey/index.html")

def result(request):
    try:
        request.session['counter']
    except(KeyError):
        request.session['counter']=1

    context = {
        'counting': request.session['counter']
    }
    request.session['counter']+=1

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favlang'] = request.POST['favlang']
    request.session['comments'] = request.POST['comments']
    return render(request,"survey/result.html",context)









 
    