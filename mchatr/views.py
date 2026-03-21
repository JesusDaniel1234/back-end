from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
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
    permission_classes = (IsAuthenticated,)
    queryset = MChatRResponses.objects.all()
    serializer_class = MChatRResponsesSerializers
