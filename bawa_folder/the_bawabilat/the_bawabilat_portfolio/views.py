from django.shortcuts import render
from .models import Newsupdate ,Post
# Create your views here.

def home(request):
    newsdata = Newsupdate.objects.all()
    blogdata = Post.objects.all()
    last_five = Newsupdate.objects.filter().order_by('-id')[:5]
    last_five_in_ascending_order = reversed(last_five)
    return render(request,'html_files/index.html',{'last_five':last_five,'blogdata':blogdata})

def homefullview(request,blog_slug):
    data_view = Newsupdate.objects.filter(blog_slug=blog_slug).first()
    print(data_view)
    return render(request,'html_files/home_view.htm',{"data_view":data_view})

def technical_news(request):
    technical_news = Newsupdate.objects.filter(blogtype__blogtype__contains="tech")
    return render(request,'html_files/Technical_news.htm',{"technical_news":technical_news})


def sports_news(request):
    sports_news = Newsupdate.objects.filter(blogtype__blogtype__contains="sport")
    return render(request,'html_files/Sports_news.htm',{'sports_news':sports_news})



def political_news(request):
    political_news = Newsupdate.objects.filter(blogtype__blogtype__contains="poli")
    return render(request,'html_files/Political_news.htm',{"political_news":political_news})

def entertainment_news(request):
    entertainment_news = Newsupdate.objects.filter(blogtype__blogtype__contains="enter")
    return render(request,'html_files/Entertainment_news.htm',{"entertainment_news":entertainment_news})

def world_wide(request):
    world_news = Newsupdate.objects.filter(blogtype__blogtype__contains="world")
    return render(request,'html_files/world_wide.htm',{"world_news":world_news})

def events(request):
    return render(request,'html_files/events.htm')

def video(request):
    video = Newsupdate.objects.all()
    blog_video = Post.objects.all()
    return render(request,'html_files/video.htm',{"video":video,"blog_video":blog_video})

def newsdatafullview(request,news_slug):
    post_view = Post.objects.filter(news_slug=news_slug).first()
    return render(request,'html_files/News_full.htm',{"post_view":post_view})

def header(request):
    newsdata = Newsupdate.objects.all()
    blog_data = Post.objects.all()
    last_five = Newsupdate.objects.filter().order_by('-id')[:5]
    last_five_in_ascending_order = reversed(last_five)
    blogdata = Post.objects.filter().order_by('-id')[:5]
    blogdata_last_five_in_ascending_order = reversed(blogdata)
    print(blogdata,last_five)
    return render(request,'html_files/header.htm',{'last_five':last_five,'blogdata':blogdata})


def contact_us(request):
    return render(request,'html_files/contact_us.htm')

def footer(request):
    newsdata = Newsupdate.objects.all()
    blog_data = Post.objects.all()
    last_five = Newsupdate.objects.filter().order_by('-id')[:5]
    last_five_in_ascending_order = reversed(last_five)
    blogdata = Post.objects.filter().order_by('-id')[:5]
    blogdata_last_five_in_ascending_order = reversed(blogdata)
    print(blogdata,last_five)
    return render(request,'html_files/footer.html',{'last_five':last_five,'blogdata':blogdata})