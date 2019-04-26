from django.http import HttpResponse
from django.shortcuts import render

def index(requeset):
	return HttpResponse("Rango says hey there partner!")
