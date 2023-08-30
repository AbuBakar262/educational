from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
        }


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
