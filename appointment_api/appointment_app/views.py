from .serializers import DoctorSerializer,PatientSerializer, AppointmentSerialaizer
from .models import Doctor, Patient, Appointment
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerialaizer

    def create(self, request, *args, **kwargs):
        appointment_date = request.get('appointment_date')
        if Appointment.objects.filter(appointment_date=appointment_date).exists():
            return Response({"message": "Already selected date available", "data": request.appointment_date})
        else:
            return Response({"message":"selected date not availble"})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def create(self, request):
    #     print(request)
    #     appointment_date = request.get('appointment_date')
    #     print(appointment_date)
    #     if Appointment.objects.filter(appointment_date=appointment_date).exists():
    #         return Response({"message": "Already selected date available", "data": request.appointment_date})
    #     else:
    #         return Response({"message":"selected date not availble"})
    #
    #














