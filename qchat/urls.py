from django.urls import path
from .views import (
    # Preguntas Q-Chat
    ListarPreguntasQChatView,
    ListarPreguntasQChatActivasView,
    DetallarPreguntasQChatView,
    CrearActualizarEliminarPreguntasQChatView,
    # Respuestas Tutor Q-Chat
    ListarRespuestasTutorQChatView,
    DetallarRespuestasTutorQChatView,
    CrearActualizarEliminarRespuestasTutorQChatView,
    # Respuestas Q-Chat
    ListarRespuestasQChatView,
    DetallarRespuestasQChatView,
    CrearActualizarEliminarRespuestasQChatView,
)

app_name = "qchat"

urlpatterns = [
    # Preguntas Qchat
    path("listar_preguntas_qchat/", ListarPreguntasQChatView.as_view()),
    path("listar_preguntasactivas_qchat", ListarPreguntasQChatActivasView.as_view()),
    path("detallar_preguntas_qchat/<int:pk>", DetallarPreguntasQChatView.as_view()),
    path("crear_preguntas_qchat/", CrearActualizarEliminarPreguntasQChatView.as_view()),
    path(
        "actualizar_preguntas_qchat/<int:pk>/",
        CrearActualizarEliminarPreguntasQChatView.as_view(),
    ),
    path(
        "eliminar_preguntas_qchat/<int:pk>",
        CrearActualizarEliminarPreguntasQChatView.as_view(),
    ),
    # Respuestas Tutor Qchat
    path("listar_respuestastutor_qchat/", ListarRespuestasTutorQChatView.as_view()),
    path(
        "detallar_respuestastutor_qchat/<int:pk>",
        DetallarRespuestasTutorQChatView.as_view(),
    ),
    path(
        "crear_respuestastutor_qchat/",
        CrearActualizarEliminarRespuestasTutorQChatView.as_view(),
    ),
    path(
        "actualizar_respuestastutor_qchat/<int:pk>/",
        CrearActualizarEliminarRespuestasTutorQChatView.as_view(),
    ),
    path(
        "eliminar_respuestastutor_qchat/<int:pk>",
        CrearActualizarEliminarRespuestasTutorQChatView.as_view(),
    ),
    # Respuestas Qchat
    path("listar_respuestas_qchat/", ListarRespuestasQChatView.as_view()),
    path("detallar_respuestas_qchat/<int:pk>", DetallarRespuestasQChatView.as_view()),
    path(
        "crear_respuestas_qchat/", CrearActualizarEliminarRespuestasQChatView.as_view()
    ),
    path(
        "actualizar_respuestas_qchat/<int:pk>/",
        CrearActualizarEliminarRespuestasQChatView.as_view(),
    ),
    path(
        "eliminar_respuestas_qchat/<int:pk>",
        CrearActualizarEliminarRespuestasQChatView.as_view(),
    ),
]
