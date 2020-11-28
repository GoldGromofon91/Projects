from rest_framework import serializers
from .models import User, AuthToken

import hashlib
from django.contrib.auth.hashers import make_password

# def transformat(us_log,us_pass):
#     """
#     Генерирует хэш-пароль + соль на основе(username)
#     """
#     hash_user_obj = hashlib.sha224(us_pass.encode('ascii'))
#     salt_hash = hashlib.sha1(us_log.encode('ascii'))
#     res_pass = hash_user_obj.hexdigest() + salt_hash.hexdigest()
#     return res_pass

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return AuthToken.objects.create(**validated_data)


class ViewSetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=150)
    first_name = serializers.CharField(max_length=30)
    last_name  = serializers.CharField(max_length=30)
    password = serializers.CharField(required=True,max_length=128)
    is_active = serializers.BooleanField(required=True)
    last_login = serializers.DateTimeField(read_only=True) 
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'], validated_data['username'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'], validated_data['username'])
        
        instance.password = validated_data.get('password', instance.password)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance