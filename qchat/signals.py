from django.db.models.signals import post_migrate, pre_delete
from .models import PreguntaQchat, RespuestasQChat
from base.models import RangoRiesgo, TipoRiesgo
from django.dispatch import receiver


@receiver(post_migrate)
def crear_preguntas_qchat(sender, **kwargs):
    if sender.name == "qchat":
        if not PreguntaQchat.objects.exists():
            preguntas = [
                {
                    "contenido": "¿Su hijo lo mira a usted cuando lo llama por su nombre?",
                    "tipo_riesgo": "Frecuencia",
                    "rango_riesgo": "Menos Frecuente",
                },
                {
                    "contenido": "¿Qué tan fácil es para usted lograr contacto visual con su hijo?",
                    "tipo_riesgo": "Facilidad",
                    "rango_riesgo": "Menos Fácil",
                },
                {
                    "contenido": "Cuando su niño está jugando solo, ¿Pone objetos en fila?",
                    "tipo_riesgo": "Tipicidad",
                    "rango_riesgo": "Menos Típico",
                },
                {
                    "contenido": "¿Pueden otras personas comprender lo que habla su hijo?",
                    "tipo_riesgo": "Frecuencia",
                    "rango_riesgo": "Menos Frecuente",
                },
                {
                    "contenido": "¿Apunta su hijo para indicar que quiere? (p.ej. Un juguete que no puede alcanzar)",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Apunta su hijo para compartir interés con usted (p. ej. Mostrar algo interesante)?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Cuánto tiempo puede mantener interés su hijo en objetos que giran?(p. ej. Lavadora, ventilador, ruedas de autos)",
                    "tipo_riesgo": "Temporal",
                    "rango_riesgo": "Menos Tiempo",
                },
                {
                    "contenido": "¿Cuántas palabras puede decir su hijo?",
                    "tipo_riesgo": "Cantidad de Palabras",
                    "rango_riesgo": "Menor Número de Palabras",
                },
                {
                    "contenido": "¿Juega su hijo a simular? (p. ej. cuidar una muñeca, hablar por un teléfono de juguete)",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Mira el niño hacia donde usted lo hace?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Con qué frecuencia su hijo huele o lame objetos inusuales?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿El niño pone la mano de usted en un objeto cuando quiere que usted lo use? (p. ej. En una manilla de una puerta para que usted la abra, en un jueguete para que usted lo encienda)",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Camina su hijo en las puntas de los pies?",
                    "tipo_riesgo": "Tipicidad",
                    "rango_riesgo": "Menos Típico",
                },
                {
                    "contenido": "¿Qué tan fácil es para su hijo adaptarse cuando se cambian sus rutinas o cuando las cosas están fuera de su lugar común?",
                    "tipo_riesgo": "Facilidad",
                    "rango_riesgo": "Menos Fácil",
                },
                {
                    "contenido": "Si usted, o alguien de la familia está visiblemente molesto, ¿Su hijo muestra signos de querer reconfortarlo? (p. ej. acariciarle el cabello, abrazarlo)",
                    "tipo_riesgo": "Tipicidad",
                    "rango_riesgo": "Menos Típico",
                },
                {
                    "contenido": "¿Su hijo repite una y otra vez algunas acciones (abrir los grifos, prender las luces abrir y cerrar puertas)?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "Usted describiría las primeras palabras de su hijo como:",
                    "tipo_riesgo": "Tipicidad",
                    "rango_riesgo": "Menos Típico",
                },
                {
                    "contenido": "¿Repite su hijo cosas que ha escuchado (cosas que usted dice frases de canciones o películas, sonidos)?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Usa su hijo gestos simples (agitar la mano para despedirse)?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Hace su hijo movimientos inusuales de los dedos cerca de sus ojos?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
                {
                    "contenido": "¿Su hijo mira espontáneamente su rostro para ver su reacción cuando se enfrenta con algo poco familiar?",
                    "tipo_riesgo": "Frecuencia",
                    "rango_riesgo": "Menos Frecuente",
                },
                {
                    "contenido": "¿Cuánto tiempo puede su hijo mantener el interés en sólo un objeto, o dos?",
                    "tipo_riesgo": "Temporal en un Día",
                    "rango_riesgo": "Menos Tiempo",
                },
                {
                    "contenido": "¿Su hijo agita objetos repetidamente (p. ej. Trozos de cuerda)?",
                    "tipo_riesgo": "Tipicidad",
                    "rango_riesgo": "Menos Típico",
                },
                {
                    "contenido": "¿Su hijo parece ser demasiado sensible al sonido?",
                    "tipo_riesgo": "Tipicidad",
                    "rango_riesgo": "Menos Típico",
                },
                {
                    "contenido": "¿Su hijo se queda mirando al vacío sin objetivo aparente?",
                    "tipo_riesgo": "Frecuencia en Periodo",
                    "rango_riesgo": "Menos Frecuente en un Periodo",
                },
            ]
            for pregunta in preguntas:
                tipo_riesgo = TipoRiesgo.objects.get(nombre=pregunta["tipo_riesgo"])
                rango_riesgo = RangoRiesgo.objects.get(rango=pregunta["rango_riesgo"], tipo_riesgo=tipo_riesgo)
                print(rango_riesgo)
                PreguntaQchat.objects.create(
                    contenido=pregunta["contenido"],
                    tipo_riesgo=tipo_riesgo,
                    rango_riesgo=rango_riesgo,
                )
@receiver(pre_delete, sender=RespuestasQChat)
def eliminar_respuestas(sender, instance, **kwargs):
    respuestas = instance.respuestas.all()
    print(f"Eliminando respuestas asociadas con {respuestas}")
    for respuesta in respuestas:
        if RespuestasQChat.objects.filter(respuestas=respuesta).count() == 1:
            print(f"Eliminando respuesta {respuesta}")
            respuesta.delete()