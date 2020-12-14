#https://medium.com/@shistory02/django-db-data%EB%A1%9C-matplotlib-plot-render%ED%95%98%EA%B8%B0-861a8e8fb93a
import os
import time

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud

from . blog.models import Post

from NRCLex import *

DATE = time.strftime('%Y-%m-%d', time.localtime(time.time()))
directory = f"../static/img/graph/{DATE}/"

def weekly_line(request):
	post_df = pd.DataFrame(list(Post.objects.all().values)) 

	plt.bar()

	if not os.path.exists(directory):
		os.makedirs(directory)
	
	plt.savefig(directory+'weekly_line.png')

def monthly_line(request):

def monthly_pi(request):

def daily_pi(request):

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