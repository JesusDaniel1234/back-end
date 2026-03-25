from rest_framework import serializers

from apps.patient.models import PatientData
from .models import MChatRResponses, MchatRQuestions


# Preguntas M-Chat-R
class MchatRQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MchatRQuestions
        fields = "__all__"


class MChatRResponsesSerializers(serializers.ModelSerializer):
    patient_name = serializers.CharField()
    CI = serializers.CharField()
    age_in_month = serializers.IntegerField()
    tutor_name = serializers.CharField()

    class Meta:
        model = MChatRResponses
        fields = "__all__"
        read_only_fields = ["puntuation"]

    def to_representation(self, instance: MChatRResponses):
        return {
            "id": instance.pk,

            "puntuation": instance.puntuation,
            "valoration": instance.valoration,
            "patient": {
                "patient_name": instance.patient.patient_name,
                "CI": instance.patient.CI,
                "age_in_month": instance.patient.age_in_month,
                "tutor_name": instance.patient.tutor_name
            },
            "responses": instance.responses
        }

    def validate_responses(self, value):
        active_question = MchatRQuestions.objects.filter(is_activa=True).count()
        if active_question != len(value):
            raise serializers.ValidationError(
                "La cantidad de respuestas no coincide con la cantidad de preguntas activas")

        for response in value:
            question = MchatRQuestions.objects.get(id=response["id"])
            if response["content"] != question.content:
                raise serializers.ValidationError("Las preguntas no coinciden")

        return value

    def _calculate_points(self, responses):
        # Se cuenta si la respuesta coincide con la respuesta de riesgo de cada pregunta
        puntuation = 0
        for response in responses:
            question = MchatRQuestions.objects.get(id=response["id"])
            if str(question.response) == str(response["response"]):
                puntuation += 1

        return puntuation

    def create(self, validated_data):
        # Datos del paciente
        patient_name = validated_data.pop("patient_name")
        CI = validated_data.pop("CI")
        age_in_month = validated_data.pop("age_in_month")
        tutor_name = validated_data.pop("tutor_name")

        # Respuestas
        responses = validated_data.pop("responses")

        patient, created = PatientData.objects.get_or_create(
            CI=CI,
            defaults={
                'patient_name': patient_name,
                'age_in_month': age_in_month,
                'tutor_name': tutor_name
            }
        )
        # Calcular Puntuación:
        puntuation = self._calculate_points(responses)

        created = MChatRResponses.objects.create(puntuation=puntuation, patient=patient, responses=responses)
        return created
