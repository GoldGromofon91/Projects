import hashlib
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from django.http import Http404

from .models import User
from .serializers import ResponseDataSerializer, UpdateDataSerializer, AuthSerializer


def transformat(us_log,us_pass):
	hash_user_obj = hashlib.sha224(us_pass.encode('ascii'))
	salt_hash = hashlib.sha1(us_log.encode('ascii'))
	res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
	return res_pass


class AuthToken(APIView):
    #Реализация GET api/v1/users
    def post (self, request):
        user_obj = request.data.get('user')
        hash_pass = transformat(user_obj['username'],user_obj['password'])
        user_obj['password'] = hash_pass
        serializer = AuthSerializer(data=user_obj)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print('Valid')
            serializer.save()
        return Response ({'token': serializer.data['password']})


class AllUsers(APIView):
    #Реализация GET api/v1/users
    def get(self, request):
        users_obj = User.objects.all()
        serializer = ResponseDataSerializer(users_obj, many=True)
        return Response({'user': serializer.data})
    # Реализация POST api/v1/users
    
    def post (self, request):
        user_obj = request.data.get('user')
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
        