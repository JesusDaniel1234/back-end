from django.urls import path, include
from .views import DetallesDatosPacienteView, DetallesPacienteYRespuestasView
from rest_framework.routers import DefaultRouter

app_name = "pacientes"

router = DefaultRouter()
router.register(r"detalles_pacientes", DetallesDatosPacienteView)

urlpatterns = [
    path("", include(router.urls)),
    path("detalles_simp/<int:pk>", DetallesPacienteYRespuestasView.as_view(), name="DetallesSimp"),
]
