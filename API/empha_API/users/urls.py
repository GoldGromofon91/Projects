from django.urls import path

from .views import AllUsers, IndividUser,AuthToken

app_name = 'users'

urlpatterns = [
    path('',AuthToken.as_view()),
    path('users/', AllUsers.as_view()),
    path('users/<int:pk>', IndividUser.as_view())
]