from django.urls import path

from .views import GetAllUsers

app_name = 'users'

urlpatterns = [
    path('users/', GetAllUsers.as_view()),
    # path('users/<int:pk>', individual_method)
]