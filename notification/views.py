from django.shortcuts import render
from notification.models import *
from rest_framework import viewsets, permissions, status
from notification.serializers import *


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NotificationSerializer
