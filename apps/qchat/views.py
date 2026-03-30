from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import QchatQuestion, QchatResponses
from .serializers import QChatResponseSerializers, QChatQuestionSerializers


# Create your views here.
class QChatQuestionViewSet(ModelViewSet):
    queryset = QchatQuestion.objects.all()

    serializer_class = QChatQuestionSerializers


class QChatResponseViewSet(ModelViewSet):
    queryset = QchatResponses.objects.all()

    serializer_class = QChatResponseSerializers

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)

        serializers.is_valid(raise_exception=True)

        serializers.save()

        return Response(serializers.data, status=status.HTTP_201_CREATED)
