from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreateSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type":"password"})
    password2 = serializers.CharField(write_only=True, required=True, style={"input_type": "password"},label="confirm password")

    class Meta:
        model = User
        fields = ['username','password','password2','email',]
        extra_kwargs ={"password":{"write_only":True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if(email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError({"email":"email address must be unique"})
        if password != password2:
            raise serializers.ValidationError({"password":"the two passwords are differ"})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
            

