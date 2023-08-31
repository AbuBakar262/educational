import io
import sys
import traceback
import requests
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Part, SubPart, Introduction, AboutUs, ContactInfo, PythonCode
from .serializers import (
    PartSerializer, IntroductionSerializer,
    AboutUsSerializer, ContactInfoSerializer,
    CompilerSerializer, SubPartSerializer
)


class IntroductionViewSet(ModelViewSet):
    """This class is used for managing endpoints for introduction"""
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    permission_classes = [permissions.AllowAny]

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
    """This class is used for managing endpoints for Part"""
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
    """This class is used for managing endpoints for Sub Parts"""
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

    def get_by_part(self, request, *args, **kwargs):
        part_id = self.request.query_params.get("part_id")
        sub_parts = SubPart.objects.filter(part_id=part_id)
        serializer = SubPartSerializer(sub_parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutUsViewSet(ModelViewSet):
    """This class is used for managing endpoints for About Us"""
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.AllowAny]

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
    """This class is used for managing endpoints for Contact Info"""
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.AllowAny]

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
    """This class is used for managing endpoints for Python compiler"""
    serializer_class = CompilerSerializer
    permission_classes = [permissions.AllowAny]

    def execute_code(self, request):
        serializer = CompilerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "success": False,
                "message": serializer.errors,
                "data": []
            }, status=status.HTTP_400_BAD_REQUEST)
        my_code = PythonCode.objects.all()[0]
        code = f"print('{my_code}')"
        original_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            exec(code)
            output = sys.stdout.getvalue()
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = original_stdout

        return Response({'output': output.replace("\n", "")}, status=status.HTTP_200_OK)
