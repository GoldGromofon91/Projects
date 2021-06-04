from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authapp.serializers import CreationUserSerializer, LoginUserSerializer


class RegistrationUserView(APIView):
    permission_classes = (AllowAny,)
    serializer = CreationUserSerializer

    def post(self, request):
        user_obj = request.data.get('user', {})
        serializer_user_data = self.serializer(data=user_obj)
        serializer_user_data.is_valid(raise_exception=True)
        serializer_user_data.save()

        return Response(serializer_user_data.data, status=status.HTTP_201_CREATED)


class LoginUserView(APIView):
    permission_classes = (AllowAny,)
    serializer = LoginUserSerializer

    def post(self, request):
        user_obj = request.data.get('user', {})
        user_data_serialize = self.serializer(data=user_obj)
        user_data_serialize.is_valid(raise_exception=True)

        return Response(user_data_serialize.data, status=status.HTTP_200_OK)
