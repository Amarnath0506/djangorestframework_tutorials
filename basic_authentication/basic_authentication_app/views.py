from .serializers import EmpSerializer
from .models import Emp
from rest_framework import viewsets


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer






