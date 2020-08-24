from rest_framework.permissions import IsAdminUser

from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet


class Emp_ViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    permission_classes = (IsAdminUser,)
