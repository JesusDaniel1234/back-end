from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import (
    PreguntasMChatR,
    RespuestaTutorMChatR,
    RespuestasMchtR,
)
from .serializers import (
    DetallarListarPreguntasMChatRSerializers,
    DetallarListarRespuestasTutorMChatRSerializers,
    EliminarActualizarCrearRespuestaTutorMChatRSerializers,
    DetallarListarRespuestasMChatRSerializers,
    EliminarActualizarCrearRespuestaMChatRSerializers,
)
from base.generador_codigo import generar_codigo
from base.models import ClaveConjunto

from pacientes.models import DatosPaciente

# Create your views here.
class GestionarPreguntasMChatRView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = PreguntasMChatR.objects.all()
    serializer_class = DetallarListarPreguntasMChatRSerializers


class ListarPreguntasMChatRActivas(ListAPIView):
    queryset = PreguntasMChatR.objects.filter(activa=True)
    serializer_class = DetallarListarPreguntasMChatRSerializers


# Respuestas Tutor M-Chat-R
class ListarRespuestasTutorMChatR(ListAPIView):
    queryset = RespuestaTutorMChatR.objects.all()
    serializer_class = DetallarListarRespuestasTutorMChatRSerializers


class DetallarRespuestasTutorMChatR(RetrieveAPIView):
    queryset = RespuestaTutorMChatR.objects.all()
    serializer_class = DetallarListarRespuestasTutorMChatRSerializers


class CrearActualizarEliminarRespuestasTutorMChatR(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):

    queryset = RespuestaTutorMChatR.objects.all()
    serializer_class = EliminarActualizarCrearRespuestaTutorMChatRSerializers

    def create(self, request, *args, **kwargs):
        while True:
            codigo = generar_codigo()
            if not ClaveConjunto.objects.filter(llave=codigo).exists():
                conjunto = ClaveConjunto.objects.create(llave=codigo)
                break
            
        for objeto in request.data:
            objeto["id_conjunto"] = conjunto.id
            serializaer = self.get_serializer(data=objeto)
            serializaer.is_valid()
            serializaer.save()
            clave = ClaveConjunto.objects.get(id=serializaer.data["id_conjunto"])
            lista_preguntas = RespuestaTutorMChatR.objects.filter(id_conjunto=clave)
            nueva_lista = []
            for elemento in lista_preguntas:
                nueva_lista.append(self.serializer_class(elemento).data["id"])

        return Response(nueva_lista, status=status.HTTP_201_CREATED)


# Respuestas M-Chat-R
class ListarRespuestasMChatR(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DetallarListarRespuestasMChatRSerializers

    def get_queryset(self):
        return RespuestasMchtR.objects.all().order_by("-fecha")


# Respuestas Tutor M-Chat-R
class DetallarRespuestasMChatR(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = RespuestasMchtR.objects.all()
    serializer_class = DetallarListarRespuestasMChatRSerializers


class CrearActualizarEliminarRespuestasMChatR(
    CreateAPIView, UpdateAPIView, DestroyAPIView
):
    queryset = RespuestasMchtR.objects.all()
    serializer_class = EliminarActualizarCrearRespuestaMChatRSerializers

    def create(self, request, *args, **kwargs):
        respuesta = DatosPaciente.objects.get(id=request.data["datos_personales"])
        if hasattr(respuesta, 'respuestasmchtr_set'):
            respuesta.respuestasmchtr_set.all().delete()
        
        return super().create(request, *args, **kwargs)