from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .views import *


router = routers.DefaultRouter()
"""""
router.register('api/token/obtain', MyTokenObtainPairView, 'token_create')
router.register('api/token/refresh/', TokenRefreshView, 'token_refresh')
router.register('api/token/verify/', TokenVerifyView, 'token_verify')
router.register('user/create/', CustomUserCreate, "create_user")
"""""
urlpatterns = router.urls
