from django.urls import path,include
from .views import EmpViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp_viewset',EmpViewSet)

urlpatterns = [
    path('',include(router.urls))
]