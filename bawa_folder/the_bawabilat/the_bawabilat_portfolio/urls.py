from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('technical-news/',views.technical_news,name="technical_news"),
    path('sports-news/',views.sports_news,name="sports_news"),
    path('political-news/',views.political_news,name="political_news"),
    path('entertainment-news/',views.entertainment_news,name="entertainment_news"),
    path('events/',views.events,name="events"),
    path('world-wide/',views.world_wide,name="world_wide"),
    path('video/',views.video,name="video"),
    path('Trending-News/<str:news_slug>/',views.newsdatafullview,name="newsdatafullview"),
    path('Current-News/<str:blog_slug>/',views.homefullview,name="homefullview"),
    path('header/',views.header,name="header"),
    path('footer/',views.footer,name="footer")

]