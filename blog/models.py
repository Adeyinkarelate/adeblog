from importlib.resources import contents
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title 
    
    # in the Pos mode, using a reverse relationship , this happen because there is relationship between the post and comment
    def comments_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    
    def __str__(self):
        return self.content 