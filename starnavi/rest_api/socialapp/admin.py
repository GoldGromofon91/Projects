from django.contrib import admin

from .models import User,Post,Likes

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Likes)