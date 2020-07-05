from django.shortcuts import render
from etatSante.models import *
from rest_framework import viewsets, permissions, status
from etatSante.serializers import *
from notification.models import *


class EtatSanteViewSet(viewsets.ModelViewSet):
    queryset = EtatSante.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EtatSanteSerializer
