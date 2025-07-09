from django.shortcuts import render

# Create your views here.

def home_view(request):
	context = {}
	return render(request, 'home.html', context)

def home_details_view(request):
	context = {}
	return render(request, 'home_details.html', context)
