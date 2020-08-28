from rest_framework import serializers
from rest_framework.serializers import ValidationError
from .models import Article


class ArticleSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def validate(self, data):
        if data['title'] == data['description']:
            raise ValidationError("title and description must be different")
        return data

    def validate_title(self, value):
        if len(value)<10:
            raise ValidationError("the value must be greater than 10")