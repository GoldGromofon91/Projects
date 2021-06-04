import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class PrototypeUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Enter username')

        if email is None:
            raise TypeError('Enter email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Enter password')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('user_name', max_length=50, unique=True)
    email = models.CharField('user_email', max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PrototypeUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'Username: {self.username}, email: {self.email}'

    @property
    def token(self):
        return self.generate_token()

    def generate_token(self):
        ttl = datetime.now() + timedelta(days=1)
        token = jwt.encode(
            {
                'id': self.pk,
                'exp': int(ttl.strftime('%s'))
             }, settings.SECRET_KEY, algorithm='HS256')
        return token

