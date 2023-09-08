from django.db import models

# Create your models here.

class blogPost(models.Model):
    blog_name = models.CharField(max_length=1000)
    blog_author = models.ForeignKey('BlogAuthor', on_delete=models.RESTRICT, null=True)
    post_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=100000)

    def __str__(self):
        return self.blog_name
    
class BlogAuthor(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name} {self.last_name}' 