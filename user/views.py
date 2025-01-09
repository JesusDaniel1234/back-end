from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import PerfilUsuario
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import (
    EliminarActualizarPerfilSerializers,
    DetallarListarPerfilSerializers,
    UserSerializers,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class ListarPerfilView(ListAPIView):
    queryset = PerfilUsuario.objects.all()
    serializer_class = DetallarListarPerfilSerializers


class DetallarPerfilView(RetrieveAPIView):
    queryset = PerfilUsuario.objects.all()
    serializer_class = DetallarListarPerfilSerializers
    

class CrearActualizarEliminarPerfilView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = PerfilUsuario.objects.all()
    serializer_class = EliminarActualizarPerfilSerializers


class CrearActualizarEliminarUserView(CreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Sesión Cerrada Correctamente"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
