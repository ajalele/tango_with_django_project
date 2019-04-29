from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context)
	
def about(request):
	context = {'boldmessage': 'This tutorial has been put together by AJ Abrahamsen.'}
	return render(request, 'rango/about.html', context)
