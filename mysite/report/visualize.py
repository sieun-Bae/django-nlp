#https://medium.com/@shistory02/django-db-data%EB%A1%9C-matplotlib-plot-render%ED%95%98%EA%B8%B0-861a8e8fb93a
import os
import time

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

from plotly.subplots import make_subplots
from plotly.offline import plot
import plotly.graph_objs as go

from PIL import Image
from io import BytesIO
from wordcloud import WordCloud
import base64

from blog.models import Post

from . import process as nlp

DATE = time.strftime('%Y-%m-%d', time.localtime(time.time()))
directory = f"./static/img/"

def weekly_bar():
	#weekly_post = list(Post.objects.all().values)
	posts = Post.objects.values()
	datas = dict()
	emotions = dict() #key: publish_date, value: score of emotions of answer1,2,3
	for post in posts:
		emotion = dict()
		print('*'+post['answer1'])
		temp = nlp.processing(str(post['answer1']) + str(post['answer2']) + str(post['answer3']))
		for k,v in temp.items():
			emotion[k] = emotion.get(k,0)+v
		emotions[post['publish_date']] = emotion
	print(emotions)

	for emotion in emotions.values():
		emotion.keys()

	fig = make_subplots(rows=5, cols=1)

	#for emotion in range(1,5):
		#fig.add_trace(go.Bar(x=labels, y=list(emotions[emotion])))
	plot_div = plot(fig, output_type='div')
	'''
	if not os.path.exists(directory):
		os.makedirs(directory)
	
	plt.savefig(directory+'weekly_line.png')
	'''
	return plot_div

#def monthly_line(request):

#def monthly_pie(request):



def daily_pie():
	emotion = dict()

	#daily_post = list(Post.objects.last().values)
	daily_post = ['', 'hi', 'enjoy watching netflix', 'I\'m happy']
	for data in daily_post[1:]:
		temp = nlp.processing(data)
		for k,v in temp.items():
			emotion[k] = emotion.get(k,0)+v
	
	labels = list(emotion.keys())
	values = list(emotion.values())
	plot_div = plot([go.Pie(labels = labels, values = values, showlegend = True, automargin = True, opacity=0.8)], output_type='div')
	
	return plot_div

def wordcloud():
	mask = np.array(Image.open(directory+'alice.png'))
	posts = Post.objects.values()
	words = str()
	for post in posts:
		temp = nlp.preprocessing(str(post['answer1']) + str(post['answer2']) + str(post['answer3']))
		words += temp
	wordcloud = WordCloud(mask = mask, background_color = 'white', max_font_size = 60, width=400, height=400).generate(words) #mask option should be added
	img=BytesIO()
	wordcloud.to_image().save(img, format='PNG')

	return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())