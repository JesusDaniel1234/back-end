from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    MyTokenObtainPairView,
    ListarRangoRiesgoView,
    ListarTipoRiesgoView,
    ListarValorRiesgoView,
    ActiveServerView, StatsViewSet, DispatchTestsViewSet
)

router = SimpleRouter()
router.register("dispatch", DispatchTestsViewSet, "dispatch")
router.register("stats", StatsViewSet, "stats")

app_name = "api"

# Rutas de la aplicación
urlpatterns = [
                  path("ok/", ActiveServerView.as_view()),
                  path("listar_valor_riesgo/", ListarValorRiesgoView.as_view()),
                  path("listar_rango_riesgo/", ListarRangoRiesgoView.as_view()),
                  path("listar_tipo_riego/", ListarTipoRiesgoView.as_view()),
                  # Token
                  path("token_obt/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
              ] + router.urls
