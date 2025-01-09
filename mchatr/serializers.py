from rest_framework import serializers
from .models import PreguntasMChatR, RespuestaTutorMChatR, RespuestasMchtR
from user.serializers import DetallarListarPerfilSerializers
from pacientes.serializers import GestionarDatosPacientesSerializers
from base.serializers import ClaveSerializers


# Preguntas M-Chat-R
class DetallarListarPreguntasMChatRSerializers(serializers.ModelSerializer):
    class Meta:
        model = PreguntasMChatR
        fields = [
            "id",
            "contenido",
            "creado_por",
            "respuesta_riesgo",
            "activa",
            "fecha_corta",
        ]

    def get_fecha_corta(self, obj):
        return obj.creado.strftime("%Y-%m-%d")


# Respuestas Tutor M-Chat-R
class DetallarListarRespuestasTutorMChatRSerializers(serializers.ModelSerializer):
    id_conjunto = ClaveSerializers()
    pregunta = DetallarListarPreguntasMChatRSerializers()

    class Meta:
        model = RespuestaTutorMChatR
        fields = "__all__"


class EliminarActualizarCrearRespuestaTutorMChatRSerializers(
    serializers.ModelSerializer
):
    class Meta:
        model = RespuestaTutorMChatR
        fields = "__all__"


# Respuestas M-Chat-R
class DetallarListarRespuestasMChatRSerializers(serializers.ModelSerializer):
    valoracion = serializers.SerializerMethodField()
    fecha_corta = serializers.SerializerMethodField()

    respuestas = DetallarListarRespuestasTutorMChatRSerializers(
        many=True, read_only=False
    )
    datos_personales = GestionarDatosPacientesSerializers()

    class Meta:
        model = RespuestasMchtR
        fields = [
            "id",
            "puntuacion",
            "respuestas",
            "datos_personales",
            "fecha_corta",
            "valoracion",
        ]

    def get_valoracion(self, obj):
        return obj.valoracion()

    def get_fecha_corta(self, obj):
        return obj.fecha.strftime("%Y-%m-%d")


class EliminarActualizarCrearRespuestaMChatRSerializers(serializers.ModelSerializer):
    class Meta:
        model = RespuestasMchtR
        fields = "__all__"


class DetallarRespuestasMChatRSimpSerializers(serializers.ModelSerializer):
    valoracion = serializers.SerializerMethodField()
    fecha_corta = serializers.SerializerMethodField()
    class Meta:
        model = RespuestasMchtR
        fields = ["id", "puntuacion", "fecha_corta", "valoracion"]
    
    def get_valoracion(self, obj):
        return obj.valoracion()

    def get_fecha_corta(self, obj):
        return obj.fecha.strftime("%Y-%m-%d")