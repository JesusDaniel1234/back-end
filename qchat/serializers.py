from rest_framework import serializers
from .models import PreguntaQchat, RespuestaTutorQChat, RespuestasQChat
from base.serializers import (
    TipoRiesgoSerializers,
    ValorRiesgoSerializers,
    RangoRiesgoSerializers,
)
from pacientes.serializers import GestionarDatosPacientesSerializers
from user.serializers import DetallarListarPerfilSerializers


# Preguntas QChat --------------------------------------------------------------------
class DetallarListarPreguntasQChatSerializers(serializers.ModelSerializer):

    obtener_valores_riesgo = serializers.SerializerMethodField()
    tipo_riesgo = TipoRiesgoSerializers()
    respuesta = ValorRiesgoSerializers()
    rango_riesgo = RangoRiesgoSerializers()

    class Meta:
        model = PreguntaQchat
        fields = [
            "contenido",
            "activa",
            "creado_por",
            "fecha_corta",
            "tipo_riesgo",
            "respuesta",
            "rango_riesgo",
            "obtener_valores_riesgo",
            "id",
        ]

    def get_obtener_valores_riesgo(self, obj):
        valores = ValorRiesgoSerializers(obj.obtener_valores_riesgo(), many=True).data
        return valores

    def get_fecha_corta(self, obj):
        return obj.creado.strftime("%Y-%m-%d")


class EliminarActualizarCrearPreguntasQChatSerializers(serializers.ModelSerializer):

    class Meta:
        model = PreguntaQchat
        fields = "__all__"


# Respuestas Tutor QChat ----------------------------------------------------------------
class DetallarListarRespuestasTutorQChatSerializers(serializers.ModelSerializer):

    pregunta = DetallarListarPreguntasQChatSerializers()
    respuesta = ValorRiesgoSerializers()

    class Meta:
        model = RespuestaTutorQChat
        fields = "__all__"


class EliminarActualizarCrearRespuestasTutorQChatSerializers(
    serializers.ModelSerializer
):

    class Meta:
        model = RespuestaTutorQChat
        fields = "__all__"


# Respuestas QChat ---------------------------------------------------------------------


class DetallarListarRespuestasQChatSerializers(serializers.ModelSerializer):

    fecha_corta = serializers.SerializerMethodField()
    respuestas = DetallarListarRespuestasTutorQChatSerializers(many=True)
    datos_personales = GestionarDatosPacientesSerializers()

    class Meta:
        model = RespuestasQChat
        fields = [
            "id",
            "puntuacion",
            "respuestas",
            "datos_personales",
            "fecha_corta",
        ]

    def get_fecha_corta(self, obj):
        return obj.fecha.strftime("%Y-%m-%d")


class EliminarActualizarCrearRespuestasQChatSerializers(serializers.ModelSerializer):

    class Meta:
        model = RespuestasQChat
        fields = [
            "id",
            "puntuacion",
            "respuestas",
            "datos_personales",
            "fecha_corta",
        ]

class DetallarRespuestasQChatSimpSerializers(serializers.ModelSerializer):
    valoracion = serializers.SerializerMethodField()
    fecha_corta = serializers.SerializerMethodField()
    class Meta:
        model = RespuestasQChat
        fields = ["id", "puntuacion", "fecha_corta", "valoracion"]
    
    def get_valoracion(self, obj):
        return obj.valoracion()

    def get_fecha_corta(self, obj):
        return obj.fecha.strftime("%Y-%m-%d")