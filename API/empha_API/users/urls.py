from django.urls import path

from .views import AllUsers, IndividUser

app_name = 'users'

urlpatterns = [
    path('users/', AllUsers.as_view()),
    path('users/<int:pk>', IndividUser.as_view())
]