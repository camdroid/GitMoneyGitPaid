from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
	return HttpResponse("Hello World!")

def windex(request):
	thing="fUcker"
	context = {'thing': thing}
	return render(request, 'index.html', context)

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(r'^home/')
        else:
            return HttpResponse("fuck")
    else:
        return HttpResponse("Invalid login, someone call the cops")

def accountHome(request):
    if request.user.is_authenticated():
        user = request.user.username
        context = {'user' : user}
        return render(request, 'profile.html', context)
    else:
        return redirect(r'^login/')