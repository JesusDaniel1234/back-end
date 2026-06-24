from rest_framework import serializers
from .models import PatientData


class PatientDataSerializers(serializers.ModelSerializer):
    valoration = serializers.ReadOnlyField()

    class Meta:
        model = PatientData
        fields = [
            "id",
            "patient_name",
            "CI",
            "age_in_month",
            "tutor_name",
            "valoration",
        ]
