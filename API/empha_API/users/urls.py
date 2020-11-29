from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet



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
    path('users/', user_list),
    path('users/<int:pk>', user_detail)
]