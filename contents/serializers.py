from rest_framework import serializers
from .models import Part, SubPart, Introduction, AboutUs, ContactInfo


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class SubPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubPart
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['part'] = PartSerializer(instance.part).data
        return representation


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
