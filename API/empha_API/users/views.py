from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404
from django.http import Http404

from .models import User
from .serializers import ResponseDataSerializer, UpdateDataSerializer


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
    
    def patch(self,request,pk):
        id_user_obj = self.get_object(pk)
        serializer = UpdateDataSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        id_user_obj = self.get_object(pk)
        id_user_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# @api_view(['GET','PUT','PATCH','DELETE'])
# def individual_method(request,pk):
#     try:
#         user_obj = User.objects.get(id=pk)
#         # print(type(user_obj), user_obj)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user_obj)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user_obj, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         user_obj_before = get_object_or_404(User.objects.all(), id=pk)
#         # print(user_obj_before)
#         data = request.data.get('user')
#         serializer = UserSerializer(instance=user_obj_before, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             user_obj_before = serializer.save()
#         return Response({'user': serializer.data})
#     elif request.method == 'DELETE':
#         user_obj.delete()
#         return Response('User deleted')