from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    return render(request,"amadon/index.html")

def purchase(request):
    values = {}
    count = 0
    purchased = 0
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken":
            values[key] = value
    try:
        values['price']
        values['quantity']
        
    except KeyError:
        pass
    request.session['price']=values['price']
    request.session['quantity']=values['quantity']
    price =request.session['price']
    quantity=request.session['quantity']
    totalprice = float(price) + float(request.session['price'])
    totalquantity = quantity + request.session['quantity']
    request.session['count']
    request.session['count']=int(request.session['count'])+int(request.session['quantity'])
    print request.session['count']
    context = {"purchased":float(price)*float(quantity),
                "totalprice":totalprice,
                "totalquantity":totalquantity
    }
    
    return render(request,"amadon/checkout.html",context)
def clear(request):
    request.session['count'].clear()
    print "clear"
    return render(request,"amadon/")