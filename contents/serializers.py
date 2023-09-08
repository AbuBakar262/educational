from rest_framework import serializers
from .models import Part, SubPart, Introduction, AboutUs, ContactInfo, PythonCode, ContactUs


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
        code_obj = PythonCode.objects.filter(sub_part=instance.id).all().order_by("id")
        new_code_list = []
        for code in code_obj:
            code_data = CompilerSerializer(code).data
            if ',' in code_data['my_code']:
                my_code = code_data['my_code'].split(',')
                code_data["my_code"] = my_code
            new_code_list.append(code_data)
        total_count = len(new_code_list)
        representation["my_code"] = new_code_list
        representation["total_my_code"] = total_count
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


class CompilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonCode
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
