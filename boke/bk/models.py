from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=30)
    createtime = models.DateTimeField(default=timezone.now)
    changetime = models.DateTimeField(auto_now=True)
    read = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    sex = models.TextField(default='男')
    age = models.IntegerField(default=18)



