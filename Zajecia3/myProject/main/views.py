from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader


# Create your views here.
def logout(request):
    request.session["logged"] = False
    request.session["user"] = ""
    request.session["try"] = 0
    return redirect('login')

def error(request):
    template = loader.get_template('error.html')
    tries = request.session.get("try", 0)
    context ={
        "try": tries
    }
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('login.html')
    login =   request.POST.get("login","")
    password =   request.POST.get("password","")
    btnSend  =   request.POST.get("btnSend", "")
    context ={}

    if(btnSend == "1"):
        if(login == "admin" and password == "admin"):
            request.session["logged"]  =   True
            request.session["user"]  =   login
            request.session["try"]   =   0
        else:
            request.session["logged"]   = False
            request.session["user"]   = ""
            request.session["try"]   = request.session.get("try", 0) + 1

        if(request.session.get('logged', False) == False):
            return redirect('error')
        else:
            return redirect('home')

    if(request.session.get('logged', False) == True):
        return redirect('home')

    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('home.html')

    logged     = request.session.get('logged', False)
    user        = request.session.get('user', False)
    context ={
        'user': user
    }

    if(logged == False):
        return redirect('login')

    return HttpResponse(template.render(context, request))



