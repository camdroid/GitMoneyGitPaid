from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World!")

def windex(request):
	thing="fUcker"
	context = {'thing': thing}
	return render(request, 'index.html', context)