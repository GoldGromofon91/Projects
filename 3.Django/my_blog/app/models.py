from django.db import models

from datetime import datetime

class Publication(models.Model):
    title = models.CharField('Название статьи', max_length = 100)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата публикации', default = datetime.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete = models.CASCADE)
    author_name = models.CharField('Автор', max_length = 50)
    text_comment = models.TextField('Текст статьи', max_length= 250)
    date_comment = models.DateTimeField('Дата комментария', default = datetime.now)


    # def __str__(self):
    #     return self.author_name

class UserListFB(models.Model):
    user_fb = models.CharField('Автор', max_length = 50)
    email_fb = models.CharField('Email',max_length = 100)
    text_fb = models.TextField('Текст статьи', max_length= 250)


class Meta:
    verbose_name = 'Публикация'
    verbose_name_plural = 'Публикации'