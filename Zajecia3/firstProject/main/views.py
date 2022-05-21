from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader


# Create your views here.
def logout(request):
    request.session["isLogged"]     =   False
    request.session["loggedAs"]     =   ""
    request.session["invalidTry"]   =   0
    return redirect("loginPage")

def loginPage(request):
    template = loader.get_template('loginPage.html')
    context ={}
    login       =   request.POST.get("login","")
    password    =   request.POST.get("password","")
    send        =   request.POST.get("send", "")
    isLoged     =   request.session.get('isLogged', False)

    if(send == "1"):
        if(login == "admin" and password == "admin"):
            request.session["isLogged"]     =   True
            request.session["loggedAs"]     =   login
            request.session["invalidTry"]   =   0
        else:
            request.session["isLogged"]     =   False
            request.session["loggedAs"]     =   ""
            request.session["invalidTry"]   =   request.session.get("invalidTry", 0) + 1

        isLoged     =   request.session.get('isLogged', False)

        if(isLoged == False):
            return redirect('invalidLogin')
        else:
            return redirect('home')

    if(isLoged == True):
        return redirect('home')

    return HttpResponse(template.render(context, request))


def home(request):
    template = loader.get_template('home.html')

    isLoged     = request.session.get('isLogged', False)
    loggedAs    = request.session.get('loggedAs', False)
    context ={
        'userName': loggedAs
    }

    if(isLoged == False):
        return redirect('loginPage')

    return HttpResponse(template.render(context, request))


def invalidLogin(request):
    template = loader.get_template('invalidLogin.html')
    invalidTry = request.session.get("invalidTry", 0)
    context ={
        "invalidTry": invalidTry
    }

    return HttpResponse(template.render(context, request))
