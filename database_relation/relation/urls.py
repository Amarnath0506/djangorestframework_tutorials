from django.urls import path,include
from .views import ParagismViewset,LanguageViewset,ProgrammerViewset


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('paragism_view',ParagismViewset)
router.register('Language_view',LanguageViewset)
router.register('Programmer_view',ProgrammerViewset)


urlpatterns = [
    path('api/', include(router.urls))

]
