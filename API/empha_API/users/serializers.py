from rest_framework import serializers
from .models import User


class ResponseDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(max_length=30)
    last_name  = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=128)
    is_active = serializers.BooleanField()
    last_login = serializers.DateTimeField() 
    is_superuser = serializers.BooleanField()
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UpdateDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True,max_length=150)
    first_name = serializers.CharField(required=False,max_length=30, default='first_name')
    last_name  = serializers.CharField(required=False,max_length=30, default='last_name')
    password = serializers.CharField(required=True,max_length=128)
    is_active = serializers.BooleanField(required=True)
    last_login = serializers.DateTimeField(required=False) 
    is_superuser = serializers.BooleanField(required=False, default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # print(validated_data)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        
        instance.save()
        return instance


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

        