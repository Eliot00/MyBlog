from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from blog.models import Article
# Create your views here.
def index(request):
    post_list = Article.objects.all()
    return render(request, 'index.html', {'post_list':post_list})