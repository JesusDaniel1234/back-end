from django.db import models
from base.models import TipoRiesgo, ValorRiesgo, RangoRiesgo, ClaveConjunto
from apps.patient.models import PatientData
from apps.user.models import UserProfile


# Create your models here.
class QchatQuestion(models.Model):
    # Datos comunes
    content = models.TextField(max_length=500)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    risk_tipe = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)
    response = models.ForeignKey(ValorRiesgo, on_delete=models.CASCADE, blank=True, null=True)
    risk_range = models.ForeignKey(RangoRiesgo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.content

    def obtener_valores_riesgo(self):
        values = ValorRiesgo.objects.filter(tipo_riesgo=self.tipo_riesgo).order_by(
            "-orden"
        )
        return values


class QchatResponses(models.Model):
    puntuation = models.PositiveIntegerField()
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
