from rest_framework import serializers
from .models import MChatRResponses, MchatRQuestions
from user.serializers import UserSerializers


# Preguntas M-Chat-R
class MchatRQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MchatRQuestions
        fields = "__all__"



class MChatRResponsesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MChatRResponses
        fields = "__all__"

    def to_representation(self, instance):
        return
