from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import PreguntaQchat, RespuestaTutorQChat, RespuestasQChat, PerfilUsuario
from base.models import TipoRiesgo, ValorRiesgo, ClaveConjunto
from base.generador_codigo import generar_codigo
from .serializers import (
    DetallarListarPreguntasQChatSerializers,
    EliminarActualizarCrearPreguntasQChatSerializers,
    DetallarListarRespuestasTutorQChatSerializers,
    EliminarActualizarCrearRespuestasTutorQChatSerializers,
    DetallarListarRespuestasQChatSerializers,
    EliminarActualizarCrearRespuestasQChatSerializers,
)
from pacientes.models import DatosPaciente

# Create your views here.


# Preguntas Qchat
class ListarPreguntasQChatView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PreguntaQchat.objects.all()
    serializer_class = DetallarListarPreguntasQChatSerializers


class ListarPreguntasQChatActivasView(ListAPIView):
    queryset = PreguntaQchat.objects.filter(activa=True)
    serializer_class = DetallarListarPreguntasQChatSerializers


class DetallarPreguntasQChatView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PreguntaQchat.objects.all()
    serializer_class = DetallarListarPreguntasQChatSerializers


class CrearActualizarEliminarPreguntasQChatView(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = PreguntaQchat.objects.all()
    serializer_class = EliminarActualizarCrearPreguntasQChatSerializers


# Respuestas Tutor Qchat -----------------------------------------------------------
class ListarRespuestasTutorQChatView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = RespuestaTutorQChat.objects.all()
    serializer_class = DetallarListarRespuestasTutorQChatSerializers


class DetallarRespuestasTutorQChatView(RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = RespuestaTutorQChat.objects.all()
    serializer_class = DetallarListarRespuestasTutorQChatSerializers


class CrearActualizarEliminarRespuestasTutorQChatView(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):
    queryset = RespuestaTutorQChat.objects.all()
    serializer_class = EliminarActualizarCrearRespuestasTutorQChatSerializers

    def create(self, request, *args, **kwargs):
        while True:
            codigo = generar_codigo()
            if not ClaveConjunto.objects.filter(llave=codigo).exists():
                conjunto = ClaveConjunto.objects.create(llave=codigo)
                break
        for objeto in request.data:
            pregunta = PreguntaQchat.objects.get(id=objeto["id"])
            tipo_riesgo = TipoRiesgo.objects.get(nombre=pregunta.tipo_riesgo)
            valor_riesgo = ValorRiesgo.objects.get(
                tipo_riesgo=tipo_riesgo, orden=objeto["value"]
            )

            objeto["id_conjunto"] = conjunto.id
            objeto["pregunta"] = objeto["id"]
            objeto["respuesta"] = valor_riesgo.id
            del objeto["id"]
            del objeto["value"]

            serializaer = self.get_serializer(data=objeto)
            serializaer.is_valid()
            serializaer.save()

            lista_preguntas = RespuestaTutorQChat.objects.filter(
                id_conjunto=serializaer.data["id_conjunto"]
            )
            nueva_lista = []

            for elemento in lista_preguntas:
                nueva_pregunta = self.serializer_class(elemento).data
                nueva_lista.append(nueva_pregunta.copy())

        return Response(nueva_lista, status=status.HTTP_201_CREATED)


# Respuestas Qchat -----------------------------------------------------------------


class ListarRespuestasQChatView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DetallarListarRespuestasQChatSerializers

    def get_queryset(self):
        return RespuestasQChat.objects.all().order_by("-fecha")


class DetallarRespuestasQChatView(RetrieveAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = RespuestasQChat.objects.all()
    serializer_class = DetallarListarRespuestasQChatSerializers


class CrearActualizarEliminarRespuestasQChatView(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):
    queryset = RespuestasQChat.objects.all()
    serializer_class = EliminarActualizarCrearRespuestasQChatSerializers

    def create(self, request, *args, **kwargs):
        respuesta = DatosPaciente.objects.get(id=request.data["datos_personales"])
        if hasattr(respuesta, 'respuestasqchat_set'):
            respuesta.respuestasqchat_set.all().delete()
        
        return super().create(request, *args, **kwargs)