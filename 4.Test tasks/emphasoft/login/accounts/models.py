from django.db import models

from datetime import datetime

class Users_reg(models.Model):
    name = models.CharField('Имя', max_length = 100)
    password = models.CharField('Пароль', max_length = 100)
    email = models.TextField('Email')
    created_at = models.DateTimeField('Дата создания', default = datetime.now)

    def __str__(self):
        return self.name


