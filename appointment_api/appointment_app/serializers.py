from rest_framework import serializers
from .models import Patient,Doctor,Appointment


def validate_name(name):
    if Patient.objects.filter(name=name):
        raise serializers.ValidationError("already this name is exists please write another name")
    else:
        return name


def validate_mobile_no(mobile_no):
    number = str(mobile_no)
    if len(number) != 10:
        raise serializers.ValidationError("provide valid mobile number")
    else:
        return mobile_no


class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])
    mobile_no =serializers.IntegerField(validators=[validate_mobile_no])

    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    books_by_author = PatientSerializer(
        read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentSerialaizer(serializers.ModelSerializer):
    Patient = PatientSerializer(read_only=True, many=True)
    Doctor = DoctorSerializer(read_only=True, many=True)
    appointment_date = serializers.DateTimeField()

    class Meta:
        model = Appointment
        fields = '__all__'






