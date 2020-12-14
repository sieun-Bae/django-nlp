from django.shortcuts import render
from .models import Post

def index(request):
	return render(request, 'index.html')

def post(request):
	return render(request, 'post.html')

def create(request):
	if(request.method == "POST"):
		post = Post() 
		post.time = request.POST['time']
		post.answer1 = request.POST['answer1']
		post.answer2 = request.POST['answer2']
		post.answer3 = request.POST['answer3']
		post.save()
	return redirect('blogs')
