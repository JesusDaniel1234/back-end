from django.db import models


# Create your models here.
class DatosPaciente(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    tarjeta_menor = models.CharField(max_length=11, unique=True,  null=False)
    edad_paciente_meses = models.PositiveIntegerField()
    nombre_tutor = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_paciente + " " + self.tarjeta_menor
