from django.db import models
from apps.base.models import TipoRiesgo, ValorRiesgo, RangoRiesgo, BaseResponse, BaseQuestion


# Create your models here.
class Qchat10Question(BaseQuestion):
    risk_type = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)

    risk_range = models.ForeignKey(RangoRiesgo, on_delete=models.CASCADE)

    risk_value = models.ForeignKey(ValorRiesgo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pregunta Q-Chat-10"

        verbose_name_plural = "Preguntas Q-Chat-10"

    @property
    def risk_values(self):
        values = ValorRiesgo.objects.filter(tipo_riesgo=self.risk_type).order_by("-orden")

        return values


class Qchat10Responses(BaseResponse):

    @property
    def valoration(self):
        return "AR" if self.puntuation > 3 else "BR"

    class Meta:
        verbose_name = "Respuesta Q-Chat-10"

        verbose_name_plural = "Respuestas Q-Chat-10"
