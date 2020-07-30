from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogType(models.Model):
    blogtype = models.CharField(max_length=200, verbose_name='Blogtype')


    def __str__(self):
        return self.blogtype

class Newsupdate(models.Model):
    Username = models.ForeignKey(User,on_delete=models.CASCADE)
    Description = models.CharField(verbose_name='News_Description',max_length=1000)
    video = EmbedVideoField()  # same like models.URLField()
    pub_date = models.DateTimeField('date published')
    blog_status = models.IntegerField(choices=STATUS, default=0)
    blog_slug = models.SlugField(max_length=200, unique=True)
    blogtype = models.ForeignKey(BlogType, on_delete=models.CASCADE)


    def __str__(self):
        return self.Description







class Post(models.Model):
    news_title = models.CharField(max_length=200, unique=True)
    news_slug = models.SlugField(max_length=200, unique=True)
    news_author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    news_updated_on = models.DateTimeField(auto_now= True)
    news_content = models.TextField()
    videos = EmbedVideoField()  # same like models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)
    news_status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.news_title
