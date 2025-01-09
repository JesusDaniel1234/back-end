from rest_framework import serializers
from .models import DatosPaciente


class GestionarDatosPacientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = DatosPaciente
        fields = "__all__"
