from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Qchat10Question, Qchat10Responses
from .serializers import QChat10ResponseSerializers, QChat10QuestionSerializers


# Create your views here.
class QChat10QuestionViewSet(ModelViewSet):
    queryset = Qchat10Question.objects.all()
    serializer_class = QChat10QuestionSerializers


class QChat10ResponseViewSet(ModelViewSet):
    queryset = Qchat10Responses.objects.all()
    serializer_class = QChat10ResponseSerializers

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)