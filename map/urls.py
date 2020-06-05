from rest_framework import routers
from django.urls import path, include
from map.views import *


router = routers.DefaultRouter()
router.register('api/region', RegionViewSet, 'region')
router.register('api/InfoRegion', InfoRegionViewSet, 'InfoRegion')
urlpatterns = router.urls
