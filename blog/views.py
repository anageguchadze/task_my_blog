from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog_view(request):
    blog_titles = ['blog post 1', 'blog post 2', 'blog post 3']
    data = {'blog_names': blog_titles}
    return render(request, 'blog/index.html', data)