from django.urls import path
from app import views

urlpatterns = [
    path('login', views.login_usr),
    path('index', views.index),
    path('registration', views.registration),
    path('all_users', views.all_users),
    ]