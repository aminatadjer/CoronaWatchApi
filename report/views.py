from django.shortcuts import render
from report.models import *
from rest_framework import viewsets, permissions, status
from report.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from sendMail.views import send
from django.http import JsonResponse
from rest_framework import viewsets, permissions, renderers


import time


from .models import *
from .serializers import *


class CasSignaleeViewSet(viewsets.ModelViewSet):
    queryset = CasSignalee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CasSignalerSerializer

    @action(methods=['post', 'get'], detail=False)
    def show_list(self, request):
        if(request.method == "GET"):
            data = CasSignalee.objects.all()
            serializers = CasSignalerSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = CasSignalerSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                send(request.data['commentaire'],
                     "Nouveau cas Signalé", "media/"+str(request.data['media']), ['ga_tadjer@esi.dz'])

                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def CasSignalerSupprimer(self, request, pk=None):
        try:
            cas = CasSignalee.objects.get(pk=pk)
        except CasSignalee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CasSignalerSerializerSupprimer(cas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['put'], detail=True)
    def CasSignalerValider(self, request, pk=None):
        try:
            cas = CasSignalee.objects.get(pk=pk)
        except CasSignalee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CasSignalerSerializerValider(cas, data=request.data)
        serializer1 = CasSignalerSerializer(cas)
        if serializer.is_valid():
            serializer.save()
            x = str(serializer1.data['media']).split("/")
            send(serializer1.data['commentaire'],
                 "Nouveau cas Signalé", "media/" + x[2], ['ga_tadjer@esi.dz'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
