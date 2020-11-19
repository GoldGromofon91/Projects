import hashlib
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from django.http import Http404

from .models import User, AuthToken
from .serializers import ResponseDataSerializer, UpdateDataSerializer, AuthSerializer
import uuid


def transformat(us_log,us_pass):
    """
    Генерирует хэш-пароль + соль на основе(username)
    """
    hash_user_obj = hashlib.sha224(us_pass.encode('ascii'))
    salt_hash = hashlib.sha1(us_log.encode('ascii'))
    res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
    return res_pass

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
            response_pswd = transformat(response_name, serializer.validated_data['password'])
            try:
                user_indb =User.objects.get(username=response_name)
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


class AllUsers(APIView):
    #Реализация GET api/v1/users
    def get(self, request):
        users_obj = User.objects.all()
        serializer = ResponseDataSerializer(users_obj, many=True)
        return Response(serializer.data)
    
    # Реализация POST api/v1/users
    def post (self, request):
        user_obj = request.data
        serializer = UpdateDataSerializer(data=user_obj)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.save()
            respserializer = ResponseDataSerializer(valid_data)
            return Response(respserializer.data)

class IndividUser(APIView):
    #Проверка на существование в БД
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    ##Реализация GET api/v1/users/pk
    def get(self, request, pk):
        user_obj = self.get_object(pk)
        serializer = ResponseDataSerializer(user_obj)
        return Response(serializer.data)
        
    #Реализация PUT api/v1/users/pk
    def put(self, request, pk):
        user_obj = self.get_object(pk)
        serializer = UpdateDataSerializer(user_obj,data=request.data)
        if serializer.is_valid():
            valid_data = serializer.save()
            respserializer = ResponseDataSerializer(valid_data)
            return Response(respserializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Реализация PATCH api/v1/users/pk
    def patch(self,request,pk):
        user_obj = self.get_object(pk)
        serializer = UpdateDataSerializer(user_obj,data=request.data, partial=True)
        if serializer.is_valid():
            valid_data = serializer.save()
            respserializer = ResponseDataSerializer(valid_data)
            return Response(respserializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Реализация DELETE api/v1/users/pk
    def delete(self, request, pk):
        user_obj = self.get_object(pk)
        user_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        