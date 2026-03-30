from django.db import models
from apps.base.models import TipoRiesgo, ValorRiesgo, RangoRiesgo, BaseQuestion, BaseResponse
from apps.patient.models import PatientData
from apps.user.models import UserProfile


# Create your models here.
class QchatQuestion(BaseQuestion):
    risk_type = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)
    risk_range = models.ForeignKey(RangoRiesgo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Pregunta Q-Chat"
        verbose_name_plural = "Preguntas Q-Chat"

    @property
    def risk_values(self):
        values = ValorRiesgo.objects.filter(tipo_riesgo=self.risk_type).order_by("-orden")
        return values


class QchatResponses(BaseResponse):

    @property
    def valoration(self):
        return "AR" if self.puntuation > 51.8 else "MR" if self.puntuation > 26.7 else "BR"

    class Meta:
        verbose_name = "Respuesta Q-Chat"
        verbose_name_plural = "Respuestas Q-Chat"
