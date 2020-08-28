from django.urls import path, include
from .views import ArticleViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('article_viewset',ArticleViewset)

urlpatterns=[
    path('articles/', include(router.urls))
]