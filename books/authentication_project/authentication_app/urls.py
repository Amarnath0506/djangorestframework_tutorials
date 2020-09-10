from django.urls import path,include
from .views import BookViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books',BookViewset)

urlpatterns = [
    path('',include(router.urls))
]
