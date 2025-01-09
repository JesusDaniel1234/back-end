from django.urls import path
from .views import (
    DetallarPerfilView,
    ListarPerfilView,
    CrearActualizarEliminarPerfilView,
    CrearActualizarEliminarUserView,
    LogoutView,
)

app_name = "usuarios"

urlpatterns = [
    # Perfil
    path("listar_perfil/", ListarPerfilView.as_view()),
    path("detallar_perfil/<int:pk>", DetallarPerfilView.as_view()),
    path("crear_perfil/", CrearActualizarEliminarPerfilView.as_view()),
    path("actualizar_perfil/<int:pk>/", CrearActualizarEliminarPerfilView.as_view()),
    path("eliminar_perfil/<int:pk>", CrearActualizarEliminarPerfilView.as_view()),
    path("logout/", LogoutView.as_view()),
    # Usuarios
    path("crear_usuario/", CrearActualizarEliminarUserView.as_view()),
    path("actualizar_usuario/<int:pk>", CrearActualizarEliminarUserView.as_view()),
    path("eliminar_usuario/<int:pk>", CrearActualizarEliminarUserView.as_view()),
]
