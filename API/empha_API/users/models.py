from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.TextField(unique=True)
    first_name = models.TextField()
    last_name  = models.TextField(default='last_name')
    password = models.TextField()
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now_add=True, blank=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username

# class AuthToken(models.Model):
#     token = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE,)

