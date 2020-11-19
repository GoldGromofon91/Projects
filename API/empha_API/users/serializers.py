from rest_framework import serializers
from .models import User, AuthToken


class ResponseDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(required=True, max_length=150)
    first_name = serializers.CharField(max_length=30)
    last_name  = serializers.CharField(max_length=30)
    password = serializers.CharField(required=True,max_length=128)
    is_active = serializers.BooleanField(required=True)
    last_login = serializers.DateTimeField(read_only=True) 
    is_superuser = serializers.BooleanField(read_only=True)
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)


class UpdateDataSerializer(serializers.Serializer):
    username = serializers.CharField(required=True,max_length=150)
    password = serializers.CharField(required=True,max_length=128)
    is_active = serializers.BooleanField(required=True)

    
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()
        return instance


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128)

    def create(self, validated_data):
        return AuthToken.objects.create(**validated_data)

        