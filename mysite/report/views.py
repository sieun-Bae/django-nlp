from django.shortcuts import render

from .visualize import daily_pie, weekly_bar, wordcloud

def report(request):
	daily_plot_div = daily_pie()
	weekly_plot_div = weekly_bar()
	word_cloud = wordcloud()
	return render(request, "report.html", \
		context={
		'daily_plot_div':daily_plot_div, 
		'weekly_plot_div':weekly_plot_div,
		'wordcloud':word_cloud
		})