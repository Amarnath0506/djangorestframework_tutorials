from .models import Article
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ArticleSerilaizer

class ArticleViewset(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerilaizer