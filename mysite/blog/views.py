from django.shortcuts import render
#from report.models import reportMain

def index(request):
	return render(request, 'index.html')

#def reportMain(request):
#	return render(request, 'reportMain.html')