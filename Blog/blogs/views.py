from django.shortcuts import render
from .models import BlogPost

def index(request):
    """The home page for Blog."""
    return render(request, 'blogs/index.html')

def posts(request):
    """Show all posts."""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    """Show a single post and all its entries."""
    post = BlogPost.objects.get(id=post_id)
    entries = post.entry_set.order_by('date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'blogs/post.html', context)