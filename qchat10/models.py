from django.db import models
from base.models import TipoRiesgo, ValorRiesgo, RangoRiesgo, ClaveConjunto
from user.models import PerfilUsuario
from pacientes.models import DatosPaciente

# Create your models here.
class PreguntasQChat10(models.Model):
    contenido = models.TextField(max_length=500)
    tipo_riesgo = models.ForeignKey(TipoRiesgo, on_delete=models.CASCADE)
    valor_riesgo = models.ForeignKey(ValorRiesgo, on_delete=models.CASCADE)
    rango_riesgo = models.ForeignKey(RangoRiesgo, on_delete=models.CASCADE)
    creado_por = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, blank=True, null=True)
    activa = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.contenido

    def obtener_valores_riesgo(self):
        valores = ValorRiesgo.objects.filter(tipo_riesgo=self.tipo_riesgo).order_by(
            "-orden"
        )
        return valores

    def fecha_corta(self):
        return self.creado.strftime("%Y-%m-%d")


class RespuestaTutorQChat10(models.Model):
    id_conjunto = models.ForeignKey(ClaveConjunto, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(PreguntasQChat10, on_delete=models.CASCADE)
    respuesta = models.ForeignKey(ValorRiesgo, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_conjunto.llave


class RespuestasQChat10(models.Model):
    puntuacion = models.PositiveIntegerField()
    respuestas = models.ManyToManyField(RespuestaTutorQChat10)
    datos_personales = models.ForeignKey(
        DatosPaciente,
        on_delete=models.CASCADE,
        verbose_name="datos_personales",
        default=1,
    )
    fecha = models.DateTimeField(auto_now_add=True)
    
    def valoracion(self):
        return "AR" if self.puntuacion > 3 else "BR"

    def fecha_corta(self):
        return self.fecha.strftime("%Y-%m-%d")

    def __str__(self):
        return self.datos_personales.nombre_paciente

