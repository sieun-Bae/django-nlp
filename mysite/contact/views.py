from django.shortcuts import render
from .models import Contact 

def contact(request):
	return render(request, 'contact.html')

def contact_q(request):
	if(request.method == "GET"):
		contact = Contact()
		contact.name = request.GET.get('name')
		contact.email = request.GET.get('email')
		contact.number = request.GET.get('number')
		contact.message = request.GET.get('message')
		contact.save()
	return redirect('contact')