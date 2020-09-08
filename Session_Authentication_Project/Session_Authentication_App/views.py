from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .serializers import EmpSerializer
from .models import Emp
from rest_framework import viewsets

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def login_form(request):
    return render(request, "login.html")

def login_user(request):
    username = request.POST['uname']
    password = request.POST['pwd']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/api')
    else:
        return redirect('/auth')


class EmpViewSet2(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
