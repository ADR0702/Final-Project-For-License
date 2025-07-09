from django.shortcuts import render

# Create your views here.

def product_list_view(request):
	context = {}
	return render(request, 'product_list.html', context)

def product_detail_view(request):
	context = {}
	return render(request, 'product_detail.html', context)
