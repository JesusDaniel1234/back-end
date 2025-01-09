from rest_framework import serializers
from .models import (
    ClaveConjunto,
    # Q-chat-100,
    TipoRiesgo,
    ValorRiesgo,
    RangoRiesgo,
)


class ClaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClaveConjunto
        fields = "__all__"


class TipoRiesgoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoRiesgo
        fields = "__all__"


class ValorRiesgoSerializers(serializers.ModelSerializer):
    tipo_riesgo = TipoRiesgoSerializers()

    class Meta:
        model = ValorRiesgo
        fields = "__all__"


class RangoRiesgoSerializers(serializers.ModelSerializer):
    tipo_riesgo = TipoRiesgoSerializers()

    class Meta:
        model = RangoRiesgo
        fields = "__all__"
