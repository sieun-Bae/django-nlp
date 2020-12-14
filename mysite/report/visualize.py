#https://medium.com/@shistory02/django-db-data%EB%A1%9C-matplotlib-plot-render%ED%95%98%EA%B8%B0-861a8e8fb93a
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from . blog.models import Post
import time

DATE = time.strftime('%Y-%m-%d', time.localtime(time.time()))

def matplotlib_graph(request):
	post_df = pd.DataFrame(list(Post.objects.all().values)) 

	plt.bar()
	plt.savefig(f'../static/img/graph/{DATE}.png')