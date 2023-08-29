from rest_framework import serializers
from .models import Part, Introduction, AboutUs, ContactInfo


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class IntroductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Introduction
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class CompilerSerializer(serializers.Serializer):
    my_code = serializers.CharField(max_length=1000)
