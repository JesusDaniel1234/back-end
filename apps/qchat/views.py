from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import QchatQuestion, QchatResponses
from base.models import TipoRiesgo, ValorRiesgo
from .serializers import QChatResponseSerializers, QChatQuestionSerializers


# Create your views here.
class QChatQuestionViewSet(ModelViewSet):
    queryset = QchatQuestion.objects.all()
    serializer_class = QChatQuestionSerializers


class QChatResponseViewSet(ModelViewSet):
    queryset = QchatResponses.objects.all()
    serializer_class = QChatResponseSerializers
