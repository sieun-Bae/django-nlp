#https://medium.com/@shistory02/django-db-data%EB%A1%9C-matplotlib-plot-render%ED%95%98%EA%B8%B0-861a8e8fb93a
import os
import time

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from plotly.offline import plot
from plotly.graph_objs import Pie
from wordcloud import WordCloud

from blog.models import Post

from . import process as nlp

DATE = time.strftime('%Y-%m-%d', time.localtime(time.time()))
directory = f"../static/img/graph/{DATE}/"

def weekly_line(request):
	post_df = pd.DataFrame(list(Post.objects.all().values)) 
	x_data = post_df['publish_date']
	plotly.offline.plot(
	)
	plt.bar()

	'''
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	plt.savefig(directory+'weekly_line.png')
	'''
	return plot_div

#def monthly_line(request):

#def monthly_pie(request):



def daily_pie():
	score = list()
	emotion = dict()

	#daily_post = list(Post.objects.last().values)
	daily_post = ['', 'hi', 'enjoy watching netflix', 'I\'m happy']
	for data in daily_post[1:]:
		temp = nlp.processing(data)
		for k,v in temp.items():
			emotion[k] = emotion.get(k,0)+v
	
	labels = list(emotion.keys())
	values = list(emotion.values())
	plot_div = plot([Pie(labels = labels, values = values, showlegend = True, automargin = True, opacity=0.8)], output_type='div')
	
	return plot_div

def wordcloud(request):
	data = Post.objects.all()
	data = NRCLex.processing(data)
	wordcloud = WordCloud(max_font_size = 100).generate(data)

	fig = plt.figure()
	plt.imshow(wordcloud, interpolation = 'bilinear')
	plt.axis('off')

	if not os.path.exists(directory):
		os.makedirs(directory)
	
	plt.savefig(directory+'wordcloud.png')