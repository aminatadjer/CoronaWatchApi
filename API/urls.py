"""API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include
from rest_framework.schemas import get_schema_view


from customauth.views import MyTokenObtainPairView, CustomUserCreate
from customauth.serializers import UserCreateSerializer
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (

    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # ...
    # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
    #   * `title` and `description` parameters are passed to `SchemaGenerator`.
    #   * Provide view name for use with `reverse()`.
    path('openapi', get_schema_view(
        title="Crona Watch Api",
        version=1.0,
        description="This API represent the backend for the CORONAWATCH school project by LOBELIAS team"
    ), name='openapi-schema'),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('map.urls')),
    path('', include('coronawatch.urls')),
    path('', include('report.urls')),
    path('', include('article.urls')),
    path('',include('customauth.urls')),
    path('', include('videos.urls')),
    path('', include('commentaire.urls')),
    path('', include('robot.urls')),
    path('api/token/obtain', MyTokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),





]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
