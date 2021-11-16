from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    photo = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title