from rest_framework import serializers
from django.contrib.auth.models import User


class UserCreateSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type":"password"})
    password2 = serializers.CharField(write_only=True, required=True, style={"input_type": "password"},label="confirm password")

    class Meta:
        model = User
        fields = ['username','email','password','password2',]
        extra_kwargs ={"password":{"write_only":True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if(email and User.objects.filter(email=email).exclude(username=username).exists()):
            
