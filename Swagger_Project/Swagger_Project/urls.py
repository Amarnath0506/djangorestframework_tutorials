"""Swagger_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from Swagger_App import views

from rest_framework_swagger.views import get_swagger_view
swagger_view = get_swagger_view(title='Employee API details')

from rest_framework.documentation import include_docs_urls
swagger_docs =include_docs_urls(title='Swagger documentation for Employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger-api/', swagger_view),
    url(r'^swagger-docs/', swagger_docs),
    url(r'^emp/$', views.Employee_List_Swagger_View.as_view()),
    url(r'^emp/(?P<pk>[0-9]+)/$', views.Employee_Detail_Swagger_View.as_view())
]
