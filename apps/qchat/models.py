from django.db import models
from base.models import TipoRiesgo, ValorRiesgo, RangoRiesgo
from apps.patient.models import PatientData
from apps.user.models import UserProfile


# Create your models here.
class QchatQuestion(models.Model):
    # Datos comunes
    content = models.TextField(max_length=500)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    risk_type = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)

    # FIXME: Ver si {response} es importante realmente
    response = models.ForeignKey(ValorRiesgo, on_delete=models.CASCADE, blank=True, null=True)
    risk_range = models.ForeignKey(RangoRiesgo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content[:50]

    @property
    def risk_values(self):
        values = ValorRiesgo.objects.filter(tipo_riesgo=self.risk_type).order_by("-orden")
        return values


class QchatResponses(models.Model):
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
        return "AR" if self.puntuation > 51.8 else "MR" if self.puntuation > 26.7 else "BR"

    def __str__(self):
        return self.patient.name
