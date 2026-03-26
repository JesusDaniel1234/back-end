from rest_framework import serializers
from .models import QchatQuestion, QchatResponses

class QChatQuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = QchatQuestion
        fields = "__all__"

class QChatResponseSerializers(serializers.ModelSerializer):
    class Meta:
        model = QchatResponses
        fields = "__all__"