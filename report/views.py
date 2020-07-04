
from rest_framework import viewsets, permissions, status

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from sendMail.views import send

from rest_framework import viewsets, permissions, renderers

from config import CCC_AGENT_EMAIL, HEALTH_AGENT_EMAIL
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
                     "Nouveau cas Signalé", "media/"+str(request.data['media']), [HEALTH_AGENT_EMAIL])

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
                 "Nouveau cas Signalé validé", "media/" + x[2], [CCC_AGENT_EMAIL])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
