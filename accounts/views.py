from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from .models import User
from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth.hashers import make_password


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def create_user(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    "message": serializer.errors,
                    "data": []
                }, status=status.HTTP_400_BAD_REQUEST)
            password = serializer.validated_data['password']
            serializer.validated_data['password'] = make_password(password)
            serializer.save()
            serializer.instance.is_superuser = True
            serializer.save()
            return Response({
                "success": True,
                "message": "User Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "success": False,
                "message": e.args[0],
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)


class UserLoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def login(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    "message": serializer.errors,
                    "data": []
                }, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.get(email=serializer.validated_data.get("email"),
                                    password=serializer.validated_data.get("password"))
            if user:
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)
                return Response({
                    "success": True,
                    "message": "Login Successfully",
                    "data": {
                        "refresh": str(refresh),
                        "access": str(access),
                        "email": user.email,
                        "password": user.password
                    }
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "success": False,
                    "message": "Invalid Credentials",
                    "data": []
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "success": False,
                "message": e.args[0],
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
