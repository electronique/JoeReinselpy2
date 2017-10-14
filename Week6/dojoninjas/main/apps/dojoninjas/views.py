from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    context={"city": Dojos.objects.all()}
    
    return render(request,"dojoninjas/index.html",context)
