from django.contrib import admin

# Register your models here.
from .models import blogPost, BlogAuthor


admin.site.register(blogPost)
admin.site.register(BlogAuthor)