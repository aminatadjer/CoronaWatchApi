from rest_framework import routers
from django.urls import path, include
from article.views import *


router = routers.DefaultRouter()
router.register('api/article', ArticleViewSet, 'article')
urlpatterns = router.urls
