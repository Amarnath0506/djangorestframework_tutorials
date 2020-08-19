from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = '__all__'


