from rest_framework import serializers
from .models import Paragism,Language,Programmer


def validated_data(name):
    if Paragism.objects.filter(name=name):
        raise serializers.ValidationError("already this name exists could you please choose another name")
    else:
        return name

def validate_max_characters(name):
    if len(name) >= 5:
        raise serializers.ValidationError("The given character is not less than 5 character please choose another word")
    else:
        return name



class ParagismSerializers(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validated_data,validate_max_characters])

    class Meta:
        model = Paragism
        fields = '__all__'




class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class ProgrammerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = '__all__'