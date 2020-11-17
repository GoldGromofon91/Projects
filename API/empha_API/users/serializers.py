from rest_framework import serializers

from .models import User
"""
1. Вьюхи декоратор на класс меняем
2. Пересмотреть валидаацию на уровне сериалайзера првоерка is_active +(возможно разбить на две части и использовать в своих вьюхах)
3. Убрать валдицаю в моделях при создании БД
3.1. Валидация хешейн а пароль
3.1.2 ПК на юсернейм
3.1.3
4. Начать писать тесты
"""
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
    username = serializers.CharField(required=True,max_length=150)
    first_name = serializers.CharField(required=False,max_length=30, default='first_name')
    last_name  = serializers.CharField(required=False,max_length=30, default='last_name')
    password = serializers.CharField(required=True,max_length=128)
    is_active = serializers.BooleanField(required=True)
    last_login = serializers.DateTimeField(required=False, default=False) 
    is_superuser = serializers.BooleanField(required=False, default=False)

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