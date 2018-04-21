from django.shortcuts import render
from .models import Post


def index(request):
	table = Post.objects.all()
	return render(request, 'index.html', {'table' : table})

