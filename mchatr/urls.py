from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GestionarPreguntasMChatRView,
    ListarRespuestasTutorMChatR,
    DetallarRespuestasTutorMChatR,
    CrearActualizarEliminarRespuestasTutorMChatR,
    ListarRespuestasMChatR,
    DetallarRespuestasMChatR,
    CrearActualizarEliminarRespuestasMChatR,
    ListarPreguntasMChatRActivas,
)


app_name = "mchatr"


router = DefaultRouter()
router.register(r"detalles_preguntas_mchatr", GestionarPreguntasMChatRView)


urlpatterns = [
    path("", include(router.urls)),
    path("listar_preguntasactivas_mchatr/", ListarPreguntasMChatRActivas.as_view()),
    # Respuestas Tutor M-Chat-R
    path("listar_respuestastutor_mchatr/", ListarRespuestasTutorMChatR.as_view()),
    path(
        "detallar_respuestastutor_mchatr/<int:pk>",
        DetallarRespuestasTutorMChatR.as_view(),
    ),
    path(
        "crear_respuestastutor_mchatr/",
        CrearActualizarEliminarRespuestasTutorMChatR.as_view(),
    ),
    path(
        "actualizar_respuestastutor_mchatr/<int:pk>/",
        CrearActualizarEliminarRespuestasTutorMChatR.as_view(),
    ),
    path(
        "eliminar_respuestastutor_mchatr/<int:pk>",
        CrearActualizarEliminarRespuestasTutorMChatR.as_view(),
    ),
    # Respuestas M-Chat-R
    path("listar_respuestas_mchatr/", ListarRespuestasMChatR.as_view()),
    path("detallar_respuestas_mchatr/<int:pk>", DetallarRespuestasMChatR.as_view()),
    path("crear_respuestas_mchatr/", CrearActualizarEliminarRespuestasMChatR.as_view()),
    path(
        "actualizar_respuestas_mchatr/<int:pk>/",
        CrearActualizarEliminarRespuestasMChatR.as_view(),
    ),
    path(
        "eliminar_respuestas_mchatr/<int:pk>",
        CrearActualizarEliminarRespuestasMChatR.as_view(),
    ),
]
