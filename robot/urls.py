from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()
router.register('api/robot/google', GoogleSearchViewSet, 'googleScrap')
router.register('api/robot/tweet', TweetsViewSet, 'tweetScrap')
router.register('api/robot/youtube', VideoYoutubeViewSet, 'youtubeScrap')
urlpatterns = router.urls
