from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def allblogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/allblogs.html', {'posts':posts})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post':post})
