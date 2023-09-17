import io
import sys
import pandas as pd
import matplotlib
import geopandas as gpd
import shapely.geometry
import contextily as ctx
import IPython
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Part, SubPart, Introduction, AboutUs, ContactInfo, PythonCode, ContactUs
from .serializers import (
    PartSerializer, IntroductionSerializer,
    AboutUsSerializer, ContactInfoSerializer,
    CompilerSerializer, SubPartSerializer,
    ContactUsSerializer
)


class IntroductionViewSet(ModelViewSet):
    """This class is used for managing endpoints for introduction"""
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create introduction
        """
        serializer = IntroductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            this endpoint will update introduction
        """
        instance = self.get_object()
        serializer = IntroductionSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            this endpoint will get single introduction by id
        """
        instance = self.get_object()
        serializer = IntroductionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
            this endpoint will list all created introduction object
        """
        queryset = Introduction.objects.all().order_by('id')
        serializer = IntroductionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PartViewSet(ModelViewSet):
    """This class is used for managing endpoints for Part"""
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create parts
        """
        serializer = PartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            this endpoint will update parts by id
        """
        instance = self.get_object()
        serializer = PartSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            this endpoint will get part by id
        """
        instance = self.get_object()
        serializer = PartSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
            this endpoint will list all created parts
        """
        queryset = Part.objects.all().order_by('id')
        serializer = PartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubPartViewSet(ModelViewSet):
    """This class is used for managing endpoints for Sub Parts"""
    queryset = SubPart.objects.all()
    serializer_class = SubPartSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create sub-parts having part in it
        """
        serializer = SubPartSerializer(data=request.data)
        if serializer.is_valid():
            part_id = serializer.validated_data.get("part").id
            # handling count for sub_parts
            count = 1
            while SubPart.objects.filter(part_id=part_id, count=f"{part_id}.{count}").exists():
                count += 1
            completed_count = f"{part_id}.{count}"
            serializer.save(count=completed_count)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            this endpoint will update sub-parts by id
        """
        instance = self.get_object()
        serializer = SubPartSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            this endpoint will get single sub-part by id
        """
        instance = self.get_object()
        serializer = SubPartSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
            this endpoint will list all the sub-parts
        """
        queryset = SubPart.objects.all().order_by('id')
        serializer = SubPartSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_part(self, request, *args, **kwargs):
        """
            this endpoint will list all the sub-parts of 1 part by giving part_id
            in the query params
        """
        part_id = self.request.query_params.get("part_id")
        sub_parts = SubPart.objects.filter(part_id=part_id).order_by('id')
        serializer = SubPartSerializer(sub_parts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutUsViewSet(ModelViewSet):
    """This class is used for managing endpoints for About Us"""
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create about us page content
        """
        serializer = AboutUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            this endpoint will update about us page content
        """
        instance = self.get_object()
        serializer = AboutUsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            this endpoint will get single about us page
        """
        instance = self.get_object()
        serializer = AboutUsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
            this endpoint will list all the about us created objects
        """
        queryset = AboutUs.objects.all().order_by('id')
        serializer = AboutUsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactInfoViewSet(ModelViewSet):
    """This class is used for managing endpoints for Contact Info"""
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create social media object including:
            facebook, instagram and youtube
        """
        serializer = ContactInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            this endpoint will update social media object including:
            facebook, instagram and youtube
        """
        instance = self.get_object()
        serializer = ContactInfoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            this endpoint will get social media object by id of:
            facebook, instagram and youtube
        """
        instance = self.get_object()
        serializer = ContactInfoSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
            this endpoint will list social media objects
        """
        queryset = ContactInfo.objects.all().order_by('id')
        serializer = ContactInfoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompilerViewSet(ModelViewSet):
    """This class is used for managing endpoints for Python compiler"""
    queryset = PythonCode.objects.all()
    serializer_class = CompilerSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create python codes
        """
        serializer = CompilerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """
            this is used for listing all the python codes.....
        """
        queryset = PythonCode.objects.all().order_by('id')
        serializer = CompilerSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def execute_code(self, request, *args, **kwargs):
        """
            This endpoint will handle execution of the code...
        """
        # instance = self.get_object()
        # my_code = instance.my_code
        # if "', p" in my_code or '", p' in my_code:
        #     list_code = my_code.split(",")
        #     output_list = []
        #     for code in list_code:
        #         original_stdout = sys.stdout
        #         sys.stdout = io.StringIO()
        #         try:
        #             exec(code)
        #             output = sys.stdout.getvalue()
        #         except Exception as e:
        #             output = str(e)
        #         finally:
        #             sys.stdout = original_stdout
        #         output_list.append(output)
        #     list_code.clear()
        #     for o in output_list:
        #         list_code.append(o.replace("\n", ""))
        #     return Response({'output': list_code}, status=status.HTTP_200_OK)
        # original_stdout = sys.stdout
        # sys.stdout = io.StringIO()
        # try:
        #     exec(my_code)
        #     output = sys.stdout.getvalue()
        # except Exception as e:
        #     output = str(e)
        # finally:
        #     sys.stdout = original_stdout
        # return Response({'output': output.replace("\n", "")}, status=status.HTTP_200_OK)
        # instance = self.get_object()
        # my_code = instance.my_code
        #
        # def execute_single_code(code):
        #     original_stdout = sys.stdout
        #     sys.stdout = io.StringIO()
        #     try:
        #         exec(code)
        #         output = sys.stdout.getvalue()
        #     except Exception as e:
        #         output = str(e)
        #     finally:
        #         sys.stdout = original_stdout
        #     if "\n" in output:
        #         return output.split("\n")
        #     return output.encode().decode('unicode_escape')
        #
        # if my_code.strip():
        #     if my_code.count("print") > 1 and "\r\n" in my_code:
        #         list_code = my_code.split("\r\n")
        #         for code in list_code:
        #             output = execute_single_code(code)
        #     else:
        #         output = execute_single_code(my_code)
        # else:
        #     output = execute_single_code(my_code)
        # if instance.image_as_output is True:
        #     url = instance.output_image.url
        #     return Response({'output': output, "url": url}, status=status.HTTP_200_OK)
        # return Response({'output': output}, status=status.HTTP_200_OK)
        instance = self.get_object()
        my_code = instance.my_code

        def execute_code(code):
            original_stdout = sys.stdout
            sys.stdout = io.StringIO()
            try:
                exec(code)
                output = sys.stdout.getvalue()
            except Exception as e:
                output = str(e)
            finally:
                sys.stdout = original_stdout
            return output.splitlines()

        if my_code.strip():
            output = execute_code(my_code)
        else:
            output = execute_code(my_code)

        if instance.image_as_output is True:
            url = instance.output_image.url
            return Response({'output': output, "url": url}, status=status.HTTP_200_OK)
        return Response({'output': output}, status=status.HTTP_200_OK)


class ContactUsViewSet(ModelViewSet):
    """This class is used for managing endpoints for Address on contact us page"""
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
            this endpoint will create address of contact us object
        """
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
            this endpoint will update address of contact us object
        """
        instance = self.get_object()
        serializer = ContactUsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        """
            this endpoint will get address of contact us object by id
        """
        instance = self.get_object()
        serializer = ContactUsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
            this endpoint will list address of contact us objects
        """
        queryset = ContactUs.objects.all().order_by('id')
        serializer = ContactUsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
