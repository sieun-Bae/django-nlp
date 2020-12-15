from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
	return render(request, 'index.html')

def post(request):
	template = 'post_success.html'
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.post_save()
			message = "Thank you for your sharing."
			return render(request, template, {"message":message})
	else:
		template = 'post.html'
		form = PostForm
		return render(request, template, {"form":form})


'''
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
'''
