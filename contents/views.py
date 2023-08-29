import os
import traceback
import requests
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Part, SubPart, Introduction, AboutUs, ContactInfo
from .serializers import (
    PartSerializer, IntroductionSerializer,
    AboutUsSerializer, ContactInfoSerializer,
    CompilerSerializer, SubPartSerializer
)


class IntroductionViewSet(ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = IntroductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IntroductionSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IntroductionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = Introduction.objects.all()
        serializer = IntroductionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PartViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = PartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PartSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PartSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = Part.objects.all()
        serializer = PartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubPartViewSet(ModelViewSet):
    queryset = SubPart.objects.all()
    serializer_class = SubPartSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = SubPartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubPartSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubPartSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = SubPart.objects.all()
        serializer = SubPartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AboutUsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AboutUsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = AboutUs.objects.all()
        serializer = AboutUsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ContactInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ContactInfoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ContactInfoSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = ContactInfo.objects.all()
        serializer = ContactInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompilerViewSet(ModelViewSet):
    serializer_class = CompilerSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            serializer = CompilerSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "success": False,
                    "message": serializer.errors,
                    "data": []
                }, status=status.HTTP_400_BAD_REQUEST)
            my_code = serializer.validated_data.get("my_code")
            url = os.getenv("COMPILER_URL")
            payload = {
                "language": os.getenv("COMPILER_LANGUAGE"),
                "version": "latest",
                "code": my_code,
                "input": None
            }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": os.getenv("RAPID_COMPILER_API_KEY"),
                "X-RapidAPI-Host": os.getenv("RAPID_COMPILER_API_HOST")
            }
            response = requests.post(url, json=payload, headers=headers)
            output = response.json().get("output").replace("\n", "")
            return Response({
                "success": True,
                "message": "Successfully compiled",
                "data": output
            }, status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()
            return Response({
                "success": False,
                "message": str(e),
                "data": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

