from django.shortcuts import render

def reportMain(request):
	return render(request, 'report.html')