from django.shortcuts import render,redirect,get_object_or_404
import django.template
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

@login_required(login_url='sign_in')
def index(request):
    blogs = Blog.objects.all().order_by("-datetime")

    return render(request, 'blogs.html', {'blogs': blogs})

@login_required(login_url='sign_in')
def add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user.username

        ins = Blog(title=title, content=content, author=user)
        ins.save()
        messages.success(request, 'Blog posted successfully')

        return redirect('/blogs')
    return render(request, 'add_blog.html')

def blog(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'single_blog.html', {'blog': blog})

