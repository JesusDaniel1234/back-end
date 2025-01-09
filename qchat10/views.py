from django.shortcuts import render
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
from .models import (
    PreguntasQChat10,
    RespuestaTutorQChat10,
    RespuestasQChat10,
)
from base.models import ClaveConjunto
from base.models import TipoRiesgo, ValorRiesgo
from base.generador_codigo import generar_codigo
from .serializers import (
    DetallarListarPreguntasQChat10Serializers,
    EliminarActualizarCrearPreguntasQChat10Serializers,
    DetallarListarRespuestasTutorQChat10Serializers,
    EliminarActualizarCrearRespuestasTutorQChat10Serializers,
    DetallarListarRespuestasQChat10Serializers,
    EliminarActualizarCrearRespuestasQChat10Serializers,
)
from pacientes.models import DatosPaciente


# Create your views here.
# Preguntas Qchat10
class ListarPreguntasQChat10View(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PreguntasQChat10.objects.all()
    serializer_class = DetallarListarPreguntasQChat10Serializers


class ListarPreguntasQChat10ActivasView(ListAPIView):
    queryset = PreguntasQChat10.objects.filter(activa=True)
    serializer_class = DetallarListarPreguntasQChat10Serializers


class DetallarPreguntasQChat10View(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PreguntasQChat10.objects.all()
    serializer_class = DetallarListarPreguntasQChat10Serializers


class CrearActualizarEliminarPreguntasQChat10View(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):
    permission_classes = (IsAuthenticated,)
    queryset = PreguntasQChat10.objects.all()
    serializer_class = EliminarActualizarCrearPreguntasQChat10Serializers


# Respuestas Tutor Qchat10 -----------------------------------------------------------
class ListarRespuestasTutorQChat10View(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RespuestaTutorQChat10.objects.all()
    serializer_class = DetallarListarRespuestasTutorQChat10Serializers


class DetallarRespuestasTutorQChat10View(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RespuestaTutorQChat10.objects.all()
    serializer_class = DetallarListarRespuestasTutorQChat10Serializers


class CrearActualizarEliminarRespuestasTutorQChat10View(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):

    queryset = RespuestaTutorQChat10.objects.all()
    serializer_class = EliminarActualizarCrearRespuestasTutorQChat10Serializers

    def create(self, request, *args, **kwargs):
        nueva_lista = []
        while True:
            codigo = generar_codigo()
            if ClaveConjunto.objects.filter(llave=codigo).exists():
                codigo = generar_codigo()
            else:
                conjunto = ClaveConjunto.objects.create(llave=codigo)
                break
        
        for objeto in request.data:
            pregunta = PreguntasQChat10.objects.get(id=objeto["id"])
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

            lista_preguntas = RespuestaTutorQChat10.objects.filter(
                id_conjunto=serializaer.data["id_conjunto"]
            )
            
            for elemento in lista_preguntas:
                nueva_pregunta = self.serializer_class(elemento).data
                nueva_lista.append(nueva_pregunta.copy())

        return Response(nueva_lista, status=status.HTTP_201_CREATED)


# Respuestas Qchat10 -----------------------------------------------------------------
class ListarRespuestasQChat10View(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = DetallarListarRespuestasQChat10Serializers
    queryset = RespuestasQChat10.objects.all().order_by("-fecha")
    


class DetallarRespuestasQChat10View(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RespuestasQChat10.objects.all()
    serializer_class = DetallarListarRespuestasQChat10Serializers


class CrearActualizarEliminarRespuestasQChat10View(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):
    queryset = RespuestasQChat10.objects.all()
    serializer_class = EliminarActualizarCrearRespuestasQChat10Serializers

    def create(self, request, *args, **kwargs):
        respuesta = DatosPaciente.objects.get(id=request.data["datos_personales"])
        if hasattr(respuesta, 'respuestasqchat10_set'):
            respuesta.respuestasqchat10_set.all().delete()
        
        return super().create(request, *args, **kwargs)
        
        
        