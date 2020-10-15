from django.contrib.auth import authenticate
from rest_framework import serializers

from authentication.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'password']


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']

    def validate(self, attrs, ):
        user = authenticate(email=attrs['email'], password=attrs['password'])
        
        if user is None:
            raise serializers.ValidationError('invalid credentials provided')
        self.instance = user
        return user