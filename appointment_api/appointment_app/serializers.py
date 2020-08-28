from rest_framework import serializers
from .models import Patient,Doctor,Appointment


class PatientSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Appointment
        fields = '__all__'
    #
    # def create(self, validated_data):
    #     appointment_date = validated_data.pop('appointment_date')
    #     appointment = Appointment.objects.create(**validated_data)
    #     Appointment.objects.create(appointment=appointment, **appointment_date)
    #     return appointment


        # try:
        #     obj = Appointment.objects.filter(appointment_date=appointment_date, doctor=doctor).exists()
        # except:
        #     return serializers.ValidationError('appointment_date with doctor already exists')





