from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Articles(models.Model):
      title=models.CharField(max_length=100)
      slug=models.SlugField()
      body=models.TextField()
      date=models.DateTimeField(auto_now_add=True)
      thumb=models.ImageField(default='default.png',blank=True)
      author=models.ForeignKey(User,default=None,   on_delete=models.CASCADE,)
def __str__(self):
    return self.title

def snippet(self):              #self pointed to the Article object
    return self.body[:50]+'....'# return only first 50 charcters and shows
