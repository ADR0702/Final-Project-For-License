from django.shortcuts import render

# Create your views here.

def login_view(request):
	context = {}
	return render(request, 'login.html', context)

def register_view(request):
	context = {}
	return render(request, 'register.html', context)

def profile_view(request):
	context = {}
	return render(request, 'profile.html', context)
