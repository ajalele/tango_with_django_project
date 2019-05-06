from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category, Page

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	page_list = Page.objects.order_by('-views')[:5]
	
	context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!', 'categories': category_list, 'pages': page_list}
	
	return render(request, 'rango/index.html', context)
	
def about(request):
	context = {'boldmessage': 'This tutorial has been put together by AJ Abrahamsen.'}
	return render(request, 'rango/about.html', context)
	
def show_category(request, category_name_slug):
	context = {}
	
	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category)
		context['pages'] = pages
		context['category'] = category
	except Category.DoesNotExist:
		context['pages'] = None
		context['category'] = None
	return render(request, 'rango/category.html', context)