from django.conf.urls import url ,include
from Pagenation_App import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp_viewset',views.EmpViewSet)

urlpatterns = [
    url(r'',include(router.urls))
]






