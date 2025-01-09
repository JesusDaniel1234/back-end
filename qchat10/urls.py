from django.urls import path
from .views import (
    # Preguntas Q-Chat
    ListarPreguntasQChat10View,
    ListarPreguntasQChat10ActivasView,
    DetallarPreguntasQChat10View,
    CrearActualizarEliminarPreguntasQChat10View,
    # Respuestas Tutor Q-Chat
    ListarRespuestasTutorQChat10View,
    DetallarRespuestasTutorQChat10View,
    CrearActualizarEliminarRespuestasTutorQChat10View,
    # Respuestas Q-Chat
    ListarRespuestasQChat10View,
    DetallarRespuestasQChat10View,
    CrearActualizarEliminarRespuestasQChat10View,
)

app_name = "qchat10"

urlpatterns = [
    # Preguntas Qchat
    path("listar_preguntas_qchat10/", ListarPreguntasQChat10View.as_view()),
    path(
        "listar_preguntasactivas_qchat10/", ListarPreguntasQChat10ActivasView.as_view()
    ),
    path("detallar_preguntas_qchat10/<int:pk>", DetallarPreguntasQChat10View.as_view()),
    path(
        "crear_preguntas_qchat10/",
        CrearActualizarEliminarPreguntasQChat10View.as_view(),
    ),
    path(
        "actualizar_preguntas_qchat10/<int:pk>/",
        CrearActualizarEliminarPreguntasQChat10View.as_view(),
    ),
    path(
        "eliminar_preguntas_qchat10/<int:pk>",
        CrearActualizarEliminarPreguntasQChat10View.as_view(),
    ),
    # Respuestas Tutor Qchat
    path("listar_respuestastutor_qchat10/", ListarRespuestasTutorQChat10View.as_view()),
    path(
        "detallar_respuestastutor_qchat10/<int:pk>",
        DetallarRespuestasTutorQChat10View.as_view(),
    ),
    path(
        "crear_respuestastutor_qchat10/",
        CrearActualizarEliminarRespuestasTutorQChat10View.as_view(),
    ),
    path(
        "actualizar_respuestastutor_qchat10/<int:pk>/",
        CrearActualizarEliminarRespuestasTutorQChat10View.as_view(),
    ),
    path(
        "eliminar_respuestastutor_qchat10/<int:pk>",
        CrearActualizarEliminarRespuestasTutorQChat10View.as_view(),
    ),
    # Respuestas Qchat
    path("listar_respuestas_qchat10/", ListarRespuestasQChat10View.as_view()),
    path(
        "detallar_respuestas_qchat10/<int:pk>", DetallarRespuestasQChat10View.as_view()
    ),
    path(
        "crear_respuestas_qchat10/",
        CrearActualizarEliminarRespuestasQChat10View.as_view(),
    ),
    path(
        "actualizar_respuestas_qchat10/<int:pk>/",
        CrearActualizarEliminarRespuestasQChat10View.as_view(),
    ),
    path(
        "eliminar_respuestas_qchat10/<int:pk>",
        CrearActualizarEliminarRespuestasQChat10View.as_view(),
    ),
]
