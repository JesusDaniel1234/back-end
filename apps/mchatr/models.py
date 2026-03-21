from django.db import models
from apps.user.models import UserProfile
from apps.patient.models import PatientData

# Create your models here.
RISK_VALUES = (("SI", "SI"), ("NO", "NO"))

class MchatRQuestions(models.Model):
    content = models.TextField("Contenido de la pregunta", max_length=500)
    response = models.CharField("Respuesta", max_length=2, choices=RISK_VALUES)
    created_by = models.ForeignKey(UserProfile, verbose_name="Usuario que creó la pregunya", on_delete=models.CASCADE,
                                   blank=True, null=True)
    is_activa = models.BooleanField("Está activa", default=True)
    created = models.DateTimeField("Creada", auto_now_add=True)
    updated = models.DateTimeField("Actualizada", auto_now=True)

    def __str__(self):
        return self.content[:50]

class MChatRResponses(models.Model):
    puntuation = models.PositiveIntegerField()
    # Hay que cambiar esto
    patient = models.ForeignKey(
        PatientData,
        on_delete=models.CASCADE,
        verbose_name="Datos del paciente",
        default=1,
    )
    created = models.DateTimeField("Creada", auto_now_add=True)
    responses = models.JSONField("Respuestas")

    @property
    def valoration(self):
        return "BR" if self.puntuation <= 3 else "MR" if self.puntuation <= 7 else "AR"

    def __str__(self):
        return self.patient.name