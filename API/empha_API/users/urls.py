from django.urls import path

from .views import AllUsers, User,Auth

app_name = 'users'

urlpatterns = [
    path('',Auth.as_view()),
    path('users/', AllUsers.as_view()),
    path('users/<int:pk>', User.as_view())
]