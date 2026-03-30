from django.db import models

from apps.patient.models import PatientData
from apps.user.models import UserProfile


class BaseQuestion(models.Model):
    content = models.TextField("Contenido de la pregunta", max_length=500)

    created_by = models.ForeignKey(UserProfile, verbose_name="Usuario que creó la pregunta", on_delete=models.CASCADE,
                                   blank=True, null=True)

    is_active = models.BooleanField("Está activa", default=True)

    created = models.DateTimeField("Creada", auto_now_add=True)

    updated = models.DateTimeField("Actualizada", auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.content[:50]


class BaseResponse(models.Model):
    puntuation = models.PositiveIntegerField("Puntuación")

    patient = models.ForeignKey(
        PatientData,
        on_delete=models.CASCADE,
        verbose_name="Datos del paciente",
        default=1,
    )
    created = models.DateTimeField("Creada", auto_now_add=True)

    responses = models.JSONField("Respuestas")

    class Meta:
        abstract = True

    def __str__(self):
        return self.patient.name


class TipoRiesgo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class ValorRiesgo(models.Model):
    valor = models.CharField(max_length=200)

    tipo_riesgo = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)

    orden = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.tipo_riesgo.nombre + " " + self.valor


class RangoRiesgo(models.Model):
    rango = models.CharField(max_length=200)

    tipo_riesgo = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.tipo_riesgo.nombre + " " + self.rango
