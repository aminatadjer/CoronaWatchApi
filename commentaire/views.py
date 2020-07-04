
from rest_framework import viewsets, permissions, status

from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from django.contrib.auth.decorators import permission_required

from rest_framework import viewsets, permissions


from .serializers import *
from .models import *


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer

    @action(methods=['post', 'get'], detail=False)
    def show_list(self, request):
        if(request.method == "GET"):
            data = Comment.objects.all()
            serializers = CommentSerializer(data, many=True)
            return Response(serializers.data)
        elif (request.method == "POST"):
            serializers = CommentSerializer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['put'], detail=True)
    def CommentSupprimer(self, request, pk=None):
        try:
            comment = Comment.objects.get(pk=pk)
        except comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializerSupprimer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

