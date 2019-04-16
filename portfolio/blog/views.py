from django.shortcuts import render
from .models import Post

# Create your views here.
def allblogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/allblogs.html', {'posts':posts})
