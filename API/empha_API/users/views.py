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
    print(token)
    return token

class Auth(APIView):
    #Реализация POST api-token-auth
    def post (self, request):
        user_obj = request.data
        serializer = AuthSerializer(data=user_obj)
        if serializer.is_valid(raise_exception=True):
            response_name = serializer.validated_data['username']
            response_pswd = serializer.validated_data['password']
            user_indb=User.objects.get(username=response_name)
            if response_name == user_indb.username and response_pswd == user_indb.password:
                token = generate_token()
                auth = AuthToken(user=user_indb,token=token)
                auth.save()
                return Response({'token':token})
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)


class AllUsers(APIView):
    #Реализация GET api/v1/users
    def get(self, request):
        users_obj = User.objects.all()
        serializer = ResponseDataSerializer(users_obj, many=True)
        return Response({'user': serializer.data})
    
    # Реализация POST api/v1/users
    def post (self, request):
        user_obj = request.data
        serializer = UpdateDataSerializer(data=user_obj)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response ({'user': serializer.data})

class IndividUser(APIView):
    #Проверка на существоавание в БД
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    ##Реализация GET api/v1/users/pk
    def get(self, request, pk):
        id_user_obj = self.get_object(pk)
        serializer = ResponseDataSerializer(id_user_obj)
        return Response(serializer.data)
        
    #Реализация PUT api/v1/users/pk
    def put(self, request, pk, format=None):
        id_user_obj = self.get_object(pk)
        if request.method == 'PUT':
            serializer = UpdateDataSerializer(id_user_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Реализация PATCH api/v1/users/pk
    def patch(self,request,pk):
        id_user_obj = self.get_object(pk)
        serializer = UpdateDataSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Реализация DELETE api/v1/users/pk
    def delete(self, request, pk, format=None):
        id_user_obj = self.get_object(pk)
        id_user_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        