from django.db import models


# Create your models here.
class PatientData(models.Model):
    patient_name = models.CharField(max_length=100)
    CI = models.CharField(max_length=11, unique=True,  null=False)
    age_in_month = models.PositiveIntegerField()
    tutor_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.patient_name + " " + self.CI
