from django.urls import path

from .views import AllUsers, IndividUser,Auth

app_name = 'users'

urlpatterns = [
    path('',Auth.as_view()),
    path('users/', AllUsers.as_view()),
    path('users/<int:pk>', IndividUser.as_view())
]