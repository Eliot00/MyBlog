from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

from blog.models import Article
# Create your views here.
def index(request):
    post_list = Article.objects.all()
    return render(request, 'index.html', {'post_list':post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'post':post})