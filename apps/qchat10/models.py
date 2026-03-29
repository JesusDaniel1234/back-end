from django.db import models
from apps.base.models import TipoRiesgo, ValorRiesgo, RangoRiesgo
from apps.user.models import UserProfile
from apps.patient.models import PatientData


# Create your models here.
class Qchat10Question(models.Model):
    # Datos comunes
    content = models.TextField("Contenido", max_length=500)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField("Activa", default=True)
    updated = models.DateTimeField("Actualizado", auto_now=True)
    risk_type = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)
    risk_range = models.ForeignKey(RangoRiesgo, on_delete=models.CASCADE)
    risk_value = models.ForeignKey(ValorRiesgo, on_delete=models.CASCADE)
    created = models.DateTimeField("Creado", auto_now_add=True)

    def __str__(self) -> str:
        return self.content[:50]

    class Meta:
        verbose_name = "Pregunta Q-Chat-10"
        verbose_name_plural = "Preguntas Q-Chat-10"

    @property
    def risk_values(self):
        values = ValorRiesgo.objects.filter(tipo_riesgo=self.risk_type).order_by("-orden")
        return values


class Qchat10Responses(models.Model):
    puntuation = models.PositiveIntegerField("Puntuación")
    responses = models.JSONField("Respuestas")
    patient = models.ForeignKey(
        PatientData,
        on_delete=models.CASCADE,
        verbose_name="Datos del paciente",
        default=1,
    )
    created = models.DateTimeField(auto_now_add=True)

    @property
    def valoration(self):
        return "AR" if self.puntuation > 3 else "BR"

    class Meta:
        verbose_name = "Respuesta Q-Chat-10"
        verbose_name_plural = "Respuestas Q-Chat-10"

    def __str__(self):
        return self.patient.name
