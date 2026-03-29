from rest_framework import serializers
from .models import (
    TipoRiesgo,
    ValorRiesgo,
    RangoRiesgo,
)



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
