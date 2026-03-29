from django.utils.autoreload import raise_last_exception
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import (
    MChatRResponses, MchatRQuestions
)
from .serializers import (
    MchatRQuestionsSerializers, MChatRResponsesSerializers
)


# Create your views here.
class MchatRQuestionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = MchatRQuestions.objects.all()
    serializer_class = MchatRQuestionsSerializers


class MChatRResponsesViewSet(viewsets.ModelViewSet):
    queryset = MChatRResponses.objects.all()
    serializer_class = MChatRResponsesSerializers

    def get_permissions(self):
        if self.action in ['update', "destroy", "list", "retrieve"]:
            return [IsAuthenticated()]
        return []


    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
