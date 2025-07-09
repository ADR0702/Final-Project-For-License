from django.shortcuts import render

# Create your views here.

def order_history_view(request):
	context = {}
	return render(request, 'order_history.html', context)
