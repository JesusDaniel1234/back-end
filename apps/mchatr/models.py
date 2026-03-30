from django.db import models
from apps.base.models import BaseQuestion, BaseResponse


class MchatRQuestions(BaseQuestion):
    RISK_VALUES = (("SI", "SI"), ("NO", "NO"))

    response = models.CharField("Respuesta", max_length=2, choices=RISK_VALUES)

    class Meta:
        verbose_name = "Pregunta M-Chat-R"

        verbose_name_plural = "Preguntas M-Chat-R"


class MChatRResponses(BaseResponse):

    @property
    def valoration(self):
        return "BR" if self.puntuation <= 3 else "MR" if self.puntuation <= 7 else "AR"

    class Meta:
        verbose_name = "Respuesta M-Chat-R"

        verbose_name_plural = "Respuestas M-Chat-R"
