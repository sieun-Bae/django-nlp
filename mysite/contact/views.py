from django.shortcuts import render
from .models import Contact 
from .forms import ContactForm
'''
def contact(request):
	return render(request, 'contact.html')

def contact_q(request):
	if(request.method == "GET"):
		contact.name = request.GET.get('name')
		contact.email = request.GET.get('email')
		contact.number = request.GET.get('number')
		contact.message = request.GET.get('message')
		contact.contact_save()
		message = "전송이 완료되었습니다."
		return render(request, 'contact_success.html', {"message":message})
	else:
		return render(request, 'contact.html')
'''
def contact(request):
	template = 'contact_success.html'
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			contact.contact_save()
			message = "전송이 완료되었습니다."
			return render(request, template, {"message":message})
	else:
		template = 'contact.html'
		form = ContactForm
		return render(request, template, {"form":form})