from django.shortcuts import render
from Pagenation_App.models import Emp
from .serializers import EmpSerializer
from rest_framework import viewsets
from .pagination import MyPagination


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
    pagination_class = MyPagination

