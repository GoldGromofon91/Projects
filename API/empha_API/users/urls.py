from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, Auth


"""
Вариант №1 наследование от APIView
"""

#  Варинт №1 
# app_name = 'users'
# urlpatterns = [
#     path('', Auth.as_view()),
#     path('users/', AllUsers.as_view()),
#     path('users/<int:pk>', User.as_view())
# ]


"""
    Исправление варианта №1 наследование от ModelViewSet
"""
user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', Auth.as_view()),
    path('users/', user_list),
    path('users/<int:pk>', user_detail)
]