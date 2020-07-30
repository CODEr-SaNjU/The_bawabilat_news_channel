from django.contrib import admin
from the_bawabilat_portfolio.models import Newsupdate,Post ,BlogType
from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.


from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_slug', 'videos','news_status','created_on')
    list_filter = ("news_status",)
    search_fields = ['news_title', 'news_content']
    prepopulated_fields = {'news_slug': ('news_title',)}
  

class NewsupdateAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Description', 'video','pub_date')
    list_filter = ("Description",)
    search_fields = ['Username', 'Description']





admin.site.register(Post, PostAdmin)
admin.site.register(BlogType)
admin.site.register(Newsupdate,NewsupdateAdmin)