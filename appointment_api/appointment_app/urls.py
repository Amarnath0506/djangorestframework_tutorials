from django.urls import path,include
from .views import PatientViewSet,DoctorViewSet,AppointmentViewset

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('patient_viewset',PatientViewSet)
router.register('doctor_viewset',DoctorViewSet)
router.register('appointment_viewset',AppointmentViewset)

urlpatterns = [
    path('',include(router.urls))
]