from django.shortcuts import render, get_object_or_404
from .models import Blog, WriterIdentifier

def all_blogs(request):
    blogs=Blog.objects.order_by('-date')
    dan=WriterIdentifier.daniels
    ste=WriterIdentifier.stefans 
    return render(request, 'blog/all_blogs.html', {'blogs':blogs, 'daniels':dan, 'stefans':ste})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
