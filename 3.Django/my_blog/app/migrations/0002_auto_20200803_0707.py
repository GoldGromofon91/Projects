# Generated by Django 3.0.4 on 2020-08-03 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.DateField(default=datetime.datetime(2020, 8, 3, 7, 7, 0, 610510), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 8, 3, 7, 7, 0, 609367), verbose_name='Дата публикации'),
        ),
    ]