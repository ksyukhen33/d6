

# Register your models here.
from django.contrib import admin
from news.models import Authors, Posts, Comment, Category, PostCategory


admin.site.register(Category)
admin.site.register(Authors)
admin.site.register(PostCategory)
admin.site.register(Posts)
admin.site.register(Comment)
