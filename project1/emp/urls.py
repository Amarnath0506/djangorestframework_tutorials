from django.urls import path
from .views import Employeelist


urlpatterns = [
    path('a/', Employeelist.as_view(), name='Employeeslist')
]
