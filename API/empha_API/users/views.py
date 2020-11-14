from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.generics import get_object_or_404


from .models import User
from .serializers import UserSerializer


class GetAllUsers(APIView):
    #Реализация GET api/v1/users
    def get(self, request):
        users_obj = User.objects.all()
        serializer = UserSerializer(users_obj, many=True)
        return Response({'user': serializer.data})
    # Реализация POST api/v1/users
    def post (self, request):
        user_obj = request.data.get('user')
        serializer = UserSerializer(data=user_obj)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response(f'User {user_saved.username} success created')

    
@api_view(['GET','PUT','PATCH','DELETE'])
def individual_method(request,pk):
    try:
        user_obj = User.objects.get(id=pk)
        # print(type(user_obj), user_obj)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user_obj)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        user_obj_before = get_object_or_404(User.objects.all(), id=pk)
        # print(user_obj_before)
        data = request.data.get('user')
        serializer = UserSerializer(instance=user_obj_before, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_obj_before = serializer.save()
        return Response({'user': serializer.data})
    elif request.method == 'DELETE':
        user_obj.delete()
        return Response('User deleted')