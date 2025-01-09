from django.db.models.signals import post_migrate, pre_delete
from .models import PreguntasQChat10, RespuestasQChat10
from base.models import RangoRiesgo, TipoRiesgo, ValorRiesgo
from django.dispatch import receiver


@receiver(post_migrate)
def crear_preguntas_qchat(sender, **kwargs):
    if sender.name == "qchat10":
        if not PreguntasQChat10.objects.exists():
            preguntas = [
                {
                    "contenido": "¿Su niño/a lo/a mira a usted cuando lo llama por su nombre?",
                    "tipo_riesgo": "Frecuencia",
                    "valor_riesgo": "A Veces",
                    "rango_riesgo": "Menos Frecuente",
                },
                {
                    "contenido": "¿Su niño/a sigue su mirada hacia donde usted está mirando?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "Algunas Veces a la Semana",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Su niño/a le mira espontáneamente a la cara para ver su reacción, cuando ocurre algo que no es habitual?",
                    "tipo_riesgo": "Frecuencia",
                    "valor_riesgo": "A Veces",
                    "rango_riesgo": "Menos Frecuente",
                },
                {
                    "contenido": "Si usted o alguien en su familia está visiblemente angustiado o triste, ¿Su niño/a muestra signos de querer ayudarlo?. Por ejemplo, acariciando su pelo o abrazándolo",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "A Veces",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Su niño/a utiliza gestos simples?. Por ejemplo, cuando se despide, ¿hace como “chao”?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "Algunas Veces a la Semana",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Que tan fácil es para usted tener contacto visual con su niño/a?. Por ejemplo, que el/ella le mire.",
                    "tipo_riesgo": "Facilidad",
                    "valor_riesgo": "Difícil",
                    "rango_riesgo": "Menos Fácil",
                },
                {
                    "contenido": "¿Su niño/a apunta con el dedo cuando quiere algo? Por ejemplo, un juguete que está fuera de su alcance.",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "Algunas Veces a la Semana",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Su niño/a juega a simular?. Por ejemplo, hacer “como si” cuidara su muñeca o “como si” hablara por un teléfono de juguete.",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "Algunas Veces a la Semana",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Su niño/a apunta con el dedo para mostrarle algo que le interesa? Por ejemplo, apunta para mostrarle o compartir algo interesante.",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "Algunas Veces a la Semana",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Tu niño/a mira a la nada, como sin propósito aparente?. Por ejemplo, mirando un punto fijo.",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": "Algunas Veces a la Semana",
                    "rango_riesgo": "Más Frecuente en un Periodo",
                },
                
            ]
            for pregunta in preguntas:
                tipo_riesgo = TipoRiesgo.objects.get(nombre=pregunta["tipo_riesgo"])
                rango_riesgo = RangoRiesgo.objects.get(rango=pregunta["rango_riesgo"])
                valor_riesgo = ValorRiesgo.objects.get(valor=pregunta["valor_riesgo"])
                print(valor_riesgo)
                PreguntasQChat10.objects.create(
                    contenido=pregunta["contenido"],
                    tipo_riesgo=tipo_riesgo,
                    rango_riesgo=rango_riesgo,
                    valor_riesgo=valor_riesgo
                )

@receiver(pre_delete, sender=RespuestasQChat10)
def eliminar_respuestas(sender, instance, **kwargs):
    respuestas = instance.respuestas.all()
    print(f"Eliminando respuestas asociadas con {respuestas}")
    for respuesta in respuestas:
        if RespuestasQChat10.objects.filter(respuestas=respuesta).count() == 1:
            print(f"Eliminando respuesta {respuesta}")
            respuesta.delete()
