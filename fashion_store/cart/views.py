from django.shortcuts import render

# Create your views here.

def cart_detail_view(request):
	context = {}
	return render(request, 'cart.html', context)
