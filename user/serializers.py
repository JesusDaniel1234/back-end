from rest_framework import serializers
from .models import PerfilUsuario
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "is_staff"]

        extra_kwargs = {
            "username": {
                "validators": [UnicodeUsernameValidator()],
            }
        }


class DetallarListarPerfilSerializers(serializers.ModelSerializer):
    usuario = UserSerializers()
    imagen_perfil = serializers.ImageField(required=False)

    class Meta:
        model = PerfilUsuario
        fields = ["id", "usuario", "imagen_perfil"]


class EliminarActualizarPerfilSerializers(serializers.ModelSerializer):
    imagen_perfil = serializers.ImageField(required=False)
    class Meta:
        model = PerfilUsuario
        fields = "__all__"
