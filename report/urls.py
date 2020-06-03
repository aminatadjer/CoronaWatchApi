from rest_framework import routers
from django.urls import path, include
from report.views import CasSignaleeViewSet


router = routers.DefaultRouter()
router.register('api/casSignaler', CasSignaleeViewSet, 'casSignaler')

urlpatterns = router.urls
