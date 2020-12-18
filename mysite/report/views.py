from django.shortcuts import render

from .visualize import daily_pie

def report(request):
	plot_div = daily_pie()
	return render(request, "report.html", context={'plot_div':plot_div})