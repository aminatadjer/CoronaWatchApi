from rest_framework import routers
from django.urls import path, include
from etatSante.views import *


router = routers.DefaultRouter()
router.register('api/etatSante', EtatSanteViewSet, 'etatSante')
urlpatterns = router.urls
