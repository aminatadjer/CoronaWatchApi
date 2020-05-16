from rest_framework import routers
from django.urls import path, include
from report.views import CasSignaleeViewSet, RegionViewSet


router = routers.DefaultRouter()
router.register('api/region', RegionViewSet, 'region')
router.register('api/casSignaler', CasSignaleeViewSet, 'casSignaler')
urlpatterns = router.urls
