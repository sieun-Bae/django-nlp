#https://medium.com/@shistory02/django-db-data%EB%A1%9C-matplotlib-plot-render%ED%95%98%EA%B8%B0-861a8e8fb93a
import os
import datetime

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

DATE = datetime.datetime.now()-datetime.timedelta(weeks=1)
directory = f"./static/img/"

def weekly_bar():
	global DATE

	posts = Post.objects.values()[:7]
	datas = dict() #key: emotion, value: [ daily emotion ]
	emotions = dict() #key: publish_date, value: score of emotions of answer1,2,3
	
	for post in posts:
		emotion = dict()
		temp = nlp.processing(str(post['answer']))
		for k,v in temp.items():
			emotion[k] = emotion.get(k,0)+v
		emotions[post['publish_date']] = emotion
	
	for i, emotion in enumerate(emotions.values()):
		for k, v in emotion.items():
			if k not in datas.keys():
				datas[k] = [0]*7
			datas[k][i] = v

	labels=list()
	for i in range(7):
		labels.append((DATE+datetime.timedelta(days=i)).strftime('%Y-%m-%d'))
		'''
	fig = make_subplots(rows=len(datas.keys()), cols=1,
		subplot_titles=list(datas.keys()), shared_xaxes=True)

	enum = [i for i in range(1,8)]
	for i, k in enumerate(datas.keys()):
		fig.add_trace(go.Bar(x=labels, y=datas[k]), row=enum[i], col=1)
	'''
	data=list()
	for k,v in datas.items():
		data.append(go.Bar(name=k, x=labels, y=v))
	fig = go.Figure(data=data)
	fig.update_layout(barmode='stack', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
	#fig.update_layout(height=800, width=600, autosize = True, showlegend=False,paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
	plot_div = plot(fig, output_type='div')
	return plot_div

def daily_pie():
	emotion = dict()

	post = Post.objects.values()[0]
	#daily_post = ['', 'hi', 'enjoy watching netflix', 'I\'m happy']
	temp = nlp.processing(str(post['answer']))
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
		temp = nlp.preprocessing(str(post['answer']))
		words += temp
	wordcloud = WordCloud(mask = mask, background_color = 'white', max_font_size = 60, width=400, height=400).generate(words) #mask option should be added
	img=BytesIO()
	wordcloud.to_image().save(img, format='PNG')

	return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())