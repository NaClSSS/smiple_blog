import markdown
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

def home(request):
    post_list = Article.objects.all()   # get all Article objects
    return render(request, 'home.html', {'post_list' :post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})

