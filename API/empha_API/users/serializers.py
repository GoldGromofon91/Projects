from rest_framework import serializers
from .models import User, AuthToken

import hashlib
from django.contrib.auth.hashers import make_password


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ['id', 'token', 'user']
    
    def create(self, validated_data):
        return AuthToken.objects.create(**validated_data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'is_active', 'last_login','is_superuser']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'], validated_data['username'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'], validated_data['username'])
        
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance
