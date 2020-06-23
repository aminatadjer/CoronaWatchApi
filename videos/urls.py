from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()
router.register('api/video', VideoViewSet, 'videoInternaut')

urlpatterns = router.urls
