from django.urls import path, include
from .views import (
    MyTokenObtainPairView,
    ListarRangoRiesgoView,
    ListarTipoRiesgoView,
    ListarValorRiesgoView,
    ListaResultadosGeneralesPorPaciente,
    ServidorActivoView
)

app_name = "api"

# Rutas de la aplicación
urlpatterns = [
    path("api_run/",ServidorActivoView.as_view()),
    path("listar_valor_riesgo/", ListarValorRiesgoView.as_view()),
    path("listar_rango_riesgo/", ListarRangoRiesgoView.as_view()),
    path("listar_tipo_riego/", ListarTipoRiesgoView.as_view()),
    path("listar_resgultados_generales/", ListaResultadosGeneralesPorPaciente.as_view()),
    # Token
    path("token_obt/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]
