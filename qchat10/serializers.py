from rest_framework import serializers
from .models import PreguntasQChat10, RespuestaTutorQChat10, RespuestasQChat10
from base.serializers import (
    TipoRiesgoSerializers,
    ValorRiesgoSerializers,
    RangoRiesgoSerializers,
)
from pacientes.serializers import GestionarDatosPacientesSerializers
from user.serializers import DetallarListarPerfilSerializers


class DetallarListarPreguntasQChat10Serializers(serializers.ModelSerializer):
    obtener_valores_riesgo = serializers.SerializerMethodField()
    tipo_riesgo = TipoRiesgoSerializers()
    valor_riesgo = ValorRiesgoSerializers()
    rango_riesgo = RangoRiesgoSerializers()

    class Meta:
        model = PreguntasQChat10
        fields = [
            "contenido",
            "activa",
            "creado_por",
            "fecha_corta",
            "tipo_riesgo",
            "valor_riesgo",
            "rango_riesgo",
            "obtener_valores_riesgo",
            "id",
        ]

    def get_obtener_valores_riesgo(self, obj):
        valores = ValorRiesgoSerializers(obj.obtener_valores_riesgo(), many=True).data
        return valores

    def get_fecha_corta(self, obj):
        return obj.creado.strftime("%Y-%m-%d")


class EliminarActualizarCrearPreguntasQChat10Serializers(serializers.ModelSerializer):

    class Meta:
        model = PreguntasQChat10
        fields = "__all__"


# Respuestas Tutor QChat ----------------------------------------------------------------
class DetallarListarRespuestasTutorQChat10Serializers(serializers.ModelSerializer):

    pregunta = DetallarListarPreguntasQChat10Serializers()
    respuesta = ValorRiesgoSerializers()

    class Meta:
        model = RespuestaTutorQChat10
        fields = "__all__"


class EliminarActualizarCrearRespuestasTutorQChat10Serializers(
    serializers.ModelSerializer
):

    class Meta:
        model = RespuestaTutorQChat10
        fields = "__all__"


# Respuestas QChat ---------------------------------------------------------------------
class DetallarListarRespuestasQChat10Serializers(serializers.ModelSerializer):

    fecha_corta = serializers.SerializerMethodField()
    respuestas = DetallarListarRespuestasTutorQChat10Serializers(many=True)
    datos_personales = GestionarDatosPacientesSerializers()

    class Meta:
        model = RespuestasQChat10
        fields = [
            "id",
            "puntuacion",
            "respuestas",
            "datos_personales",
            "fecha_corta",
        ]

    def get_fecha_corta(self, obj):
        return obj.fecha.strftime("%Y-%m-%d")


class EliminarActualizarCrearRespuestasQChat10Serializers(serializers.ModelSerializer):

    class Meta:
        model = RespuestasQChat10
        fields = [
            "id",
            "puntuacion",
            "respuestas",
            "datos_personales",
            "fecha_corta",
        ]

class DetallarRespuestasQChat10SimpSerializers(serializers.ModelSerializer):
    fecha_corta = serializers.SerializerMethodField()
    valoracion = serializers.SerializerMethodField()
    class Meta:
        model = RespuestasQChat10
        fields = ["id", "puntuacion", "fecha_corta", "valoracion"]
    
    def get_valoracion(self, obj):
        return obj.valoracion()

    def get_fecha_corta(self, obj):
        return obj.fecha.strftime("%Y-%m-%d")