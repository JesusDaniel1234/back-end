from django.db import models


# Create your models here.
class ClaveConjunto(models.Model):
    llave = models.CharField(max_length=10)

    def __str__(self):
        return self.llave


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
