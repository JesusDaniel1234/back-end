from django.db import models
from user.models import PerfilUsuario
from base.models import ClaveConjunto
from pacientes.models import DatosPaciente

# Create your models here.
VALORES_RIESGO = (("SI", "SI"), ("NO", "NO"))


class PreguntasMChatR(models.Model):
    contenido = models.TextField(max_length=500)
    respuesta_riesgo = models.CharField(max_length=2, choices=VALORES_RIESGO)
    creado_por = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE, blank=True, null=True)
    activa = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def fecha_corta(self):
        return self.creado.strftime("%Y-%m-%d")

    def __str__(self):
        return self.contenido[:50]


class RespuestaTutorMChatR(models.Model):
    id_conjunto = models.ForeignKey(ClaveConjunto, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(PreguntasMChatR, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=2, choices=VALORES_RIESGO)

    def __str__(self):
        return self.id_conjunto.llave


VALORACION = (("BR", "BR"), ("MR", "MR"), ("AR", "AR"))


class RespuestasMchtR(models.Model):
    puntuacion = models.PositiveIntegerField()
    respuestas = models.ManyToManyField(RespuestaTutorMChatR)
    datos_personales = models.ForeignKey(
        DatosPaciente,
        on_delete=models.CASCADE,
        verbose_name="datos_personales",
        default=1,
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def valoracion(self):
        if self.puntuacion <= 3:
            return "BR"
        elif self.puntuacion >= 4 and self.puntuacion <= 7:
            return "MR"
        return "AR"

    def fecha_corta(self):
        return self.fecha.strftime("%Y-%m-%d")

    def __str__(self):
        return self.datos_personales.nombre_paciente

# @receiver(post_delete, sender=RespuestasMchtR)
# @receiver(post_delete, sender=RespuestasQChat)
# def delete_paciente_if_no_responses(sender, instance, **kwargs):
#     datos_paciente = instance.datos_personales
#     mcht_responses_count = RespuestasMchtR.objects.filter(datos_personales=datos_paciente).count()
#     qchat_responses_count = RespuestasQChat.objects.filter(datos_personales=datos_paciente).count()

#     if mcht_responses_count == 0 and qchat_responses_count == 0:
#         datos_paciente.delete()