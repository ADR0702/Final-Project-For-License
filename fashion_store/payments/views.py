from django.shortcuts import render

# Create your views here.

def process_payment_view(request):
	context = {}
	return render(request, 'payment.html', context)
