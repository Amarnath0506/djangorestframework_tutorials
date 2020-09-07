from .serializers import ParagismSerializers,LanguageSerializers,ProgrammerSerializers
from .models import Paragism,Programmer,Language
from rest_framework import viewsets


class ParagismViewset(viewsets.ModelViewSet):
    queryset = Paragism.objects.all()
    serializer_class = ParagismSerializers


class LanguageViewset(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers


class ProgrammerViewset(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializers
