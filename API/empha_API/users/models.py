from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, default='first_name')
    last_name  = models.CharField(max_length=30, default='last_name')
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class AuthToken(models.Model):
    token = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,)

