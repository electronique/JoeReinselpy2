from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def blog_post(request,number):
    response = "Placeholder for blog post"+str(number)
    return HttpResponse(response)
def blog_post_edit(request,number):
    response = "Placeholder for edit blog post"+str(number)
    return HttpResponse(response)
def destroy(request,number):
    return redirect('/')
def create(request):
    
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"
   
        return redirect('/')  # more on session below
