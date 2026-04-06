from .models import Qchat10Responses, Qchat10Question
from rest_framework import serializers

from ..base.models import ValorRiesgo, TipoRiesgo
from ..base.serializers import ValorRiesgoSerializers
from ..patient.models import PatientData


class QChat10QuestionSerializers(serializers.ModelSerializer):
    risk_values = serializers.SerializerMethodField()

    def get_risk_values(self, obj):
        queryset = obj.risk_values
        values = ValorRiesgoSerializers(queryset, many=True).data
        return [item["valor"] for item in values]

    class Meta:
        model = Qchat10Question

        fields = "__all__"


class QChat10ResponseSerializers(serializers.ModelSerializer):
    patient_name = serializers.CharField()

    CI = serializers.CharField()

    age_in_month = serializers.IntegerField()

    tutor_name = serializers.CharField()

    class Meta:

        model = Qchat10Responses

        fields = "__all__"

        read_only_fields = ["puntuation"]

    def to_representation(self, instance: Qchat10Responses):

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

        active_question = Qchat10Question.objects.filter(is_active=True).count()

        if active_question != len(value):
            raise serializers.ValidationError(
                f"La cantidad de respuestas no coincide con la cantidad de preguntas activas")

        for response in value:

            question = Qchat10Question.objects.get(id=response["id"])

            if response["content"] != question.content:
                raise serializers.ValidationError("Las preguntas no coinciden")

        return value

    def _calculate_points(self, responses):
        # Cada respuesta tiene un valor especifico y el riesgo se determina con la sumatoria de dicho riesgo
        puntuation = 0
        for response in responses:

            question = Qchat10Question.objects.get(id=response["id"])

            is_less_risk = question.risk_range.rango.startswith("Menos")

            risk_type = TipoRiesgo.objects.get(nombre=question.risk_type)

            risk_value = ValorRiesgo.objects.get(valor=response["response"], tipo_riesgo=risk_type)

            is_value_in_risk_range = (

                question.risk_value.orden >= int(risk_value.orden)

                if is_less_risk

                else question.risk_value.orden <= int(risk_value.orden)

            )

            if is_value_in_risk_range:
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

        created = Qchat10Responses.objects.create(puntuation=puntuation, patient=patient, responses=responses)
        return created
