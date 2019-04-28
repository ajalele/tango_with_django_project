from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context)
	
def about(request):
	return HttpResponse('Rango says here is the about page.<br />Check out the about page -> <a href="/rango/">Index</a>')
