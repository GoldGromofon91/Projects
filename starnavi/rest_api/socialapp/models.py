from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    username = models.CharField('username', max_length=128, unique=True)
    password = models.IntegerField('password', default=111)

    def __str__(self):
        return f"Name: {self.username}"


class Post(models.Model):
    title = models.CharField('title', max_length=120, blank=True)
    description = models.CharField('description', max_length=128, blank=True)
    body = models.TextField('body', blank=True)
    author = models.ForeignKey('User', related_name='post', on_delete=models.CASCADE)

    def __str__(self):
        return f"Post Title: {self.title}"


# TODO подумать над моделью лайков!!!
class Likes(models.Model):
    post = models.OneToOneField('Post', on_delete=models.CASCADE)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
