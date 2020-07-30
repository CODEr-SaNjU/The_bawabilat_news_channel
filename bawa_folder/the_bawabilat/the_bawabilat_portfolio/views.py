from django.shortcuts import render
from .models import Newsupdate ,Post
# Create your views here.

def home(request):
    newsdata = Newsupdate.objects.all()
    blogdata = Post.objects.all()
    last_five = Newsupdate.objects.filter().order_by('-id')[:5]
    last_five_in_ascending_order = reversed(last_five)
    return render(request,'html_files/index.html',{'last_five':last_five,'blogdata':blogdata})


def technical_news(request):
    return render(request,'html_files/Technical_news.htm')


def sports_news(request):
    return render(request,'html_files/Sports_news.htm')



def political_news(request):
    return render(request,'html_files/Political_news.htm')

def entertainment_news(request):
    return render(request,'html_files/Entertainment_news.htm')

def world_wide(request):
    return render(request,'html_files/world_wide.htm')

def events(request):
    return render(request,'html_files/events.htm')

def video(request):
    return render(request,'html_files/video.htm')

def newsdatafullview(request,news_slug):
    post_view = Post.objects.filter(news_slug=news_slug).first()
    return render(request,'html_files/News_full.htm',{"post_view":post_view})