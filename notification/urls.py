from rest_framework import routers
from django.urls import path, include
from notification.views import *


router = routers.DefaultRouter()
router.register('api/notification', NotificationViewSet, 'notification')
urlpatterns = router.urls
