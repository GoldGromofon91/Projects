import uuid
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from django.http import Http404
from rest_framework import viewsets

from .models import User, AuthToken
from .serializers import AuthSerializer, UserSerializer
from django.contrib.auth.hashers import make_password

from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated


def generate_token():
    """Генерация ТОКЕНА """
    token = uuid.uuid4().hex[:32]
    return token


class Auth(APIView):
    #Реализация POST api-token-auth
    def post (self, request):
        user_obj = request.data
        serializer = AuthSerializer(data=user_obj)
        if serializer.is_valid(raise_exception=True):
            response_name = serializer.validated_data['username']
            response_pswd = make_password(serializer.validated_data['password'], response_name)
            try:
                user_indb = User.objects.get(username=response_name)
            except User.DoesNotExist:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            if response_name == user_indb.username and response_pswd == user_indb.password:
                token = generate_token()
                auth = AuthToken(user=user_indb,token=token)
                auth.save()
                user_indb.is_active = 'True'
                return Response({'token':token})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
