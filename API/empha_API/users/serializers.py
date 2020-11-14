from rest_framework import serializers

from .models import User
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name  = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField(default=False)
    last_login = serializers.DateTimeField()
    is_superuser = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.last_login = validated_data.get('last_login', instance.last_login)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
        
        instance.save()
        return instance