from .views import EmpViewSet2
from django.conf.urls import url,include

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp_viewset',EmpViewSet2)

urlpatterns = [
    url(r'emp/',include(router.urls))
]