from django.db.models.signals import post_migrate
from .models import QchatQuestion
from apps.base.models import RangoRiesgo, TipoRiesgo
from django.dispatch import receiver
from django.db import OperationalError, ProgrammingError


@receiver(post_migrate)
def create_questions_qchat(sender, **kwargs):
    if sender.name == "apps.qchat":
        try:
            if not QchatQuestion.objects.exists():

                questions = [
                    {
                        "content": "¿Su hijo lo mira a usted cuando lo llama por su nombre?",
                        "risk_type": "Frecuencia",
                        "risk_range": "Menos Frecuente",
                    },
                    {
                        "content": "¿Qué tan fácil es para usted lograr contacto visual con su hijo?",
                        "risk_type": "Facilidad",
                        "risk_range": "Menos Fácil",
                    },
                    {
                        "content": "Cuando su niño está jugando solo, ¿Pone objetos en fila?",
                        "risk_type": "Tipicidad",
                        "risk_range": "Menos Típico",
                    },
                    {
                        "content": "¿Pueden otras personas comprender lo que habla su hijo?",
                        "risk_type": "Frecuencia",
                        "risk_range": "Menos Frecuente",
                    },
                    {
                        "content": "¿Apunta su hijo para indicar que quiere? (p.ej. Un juguete que no puede alcanzar)",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Apunta su hijo para compartir interés con usted (p. ej. Mostrar algo interesante)?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Cuánto tiempo puede mantener interés su hijo en objetos que giran?(p. ej. Lavadora, ventilador, ruedas de autos)",
                        "risk_type": "Temporal",
                        "risk_range": "Menos Tiempo",
                    },
                    {
                        "content": "¿Cuántas palabras puede decir su hijo?",
                        "risk_type": "Cantidad de Palabras",
                        "risk_range": "Menor Número de Palabras",
                    },
                    {
                        "content": "¿Juega su hijo a simular? (p. ej. cuidar una muñeca, hablar por un teléfono de juguete)",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Mira el niño hacia donde usted lo hace?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Con qué frecuencia su hijo huele o lame objetos inusuales?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿El niño pone la mano de usted en un objeto cuando quiere que usted lo use? (p. ej. En una manilla de una puerta para que usted la abra, en un jueguete para que usted lo encienda)",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Camina su hijo en las puntas de los pies?",
                        "risk_type": "Tipicidad",
                        "risk_range": "Menos Típico",
                    },
                    {
                        "content": "¿Qué tan fácil es para su hijo adaptarse cuando se cambian sus rutinas o cuando las cosas están fuera de su lugar común?",
                        "risk_type": "Facilidad",
                        "risk_range": "Menos Fácil",
                    },
                    {
                        "content": "Si usted, o alguien de la familia está visiblemente molesto, ¿Su hijo muestra signos de querer reconfortarlo? (p. ej. acariciarle el cabello, abrazarlo)",
                        "risk_type": "Tipicidad",
                        "risk_range": "Menos Típico",
                    },
                    {
                        "content": "¿Su hijo repite una y otra vez algunas acciones (abrir los grifos, prender las luces abrir y cerrar puertas)?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "Usted describiría las primeras palabras de su hijo como:",
                        "risk_type": "Tipicidad",
                        "risk_range": "Menos Típico",
                    },
                    {
                        "content": "¿Repite su hijo cosas que ha escuchado (cosas que usted dice frases de canciones o películas, sonidos)?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Usa su hijo gestos simples (agitar la mano para despedirse)?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Hace su hijo movimientos inusuales de los dedos cerca de sus ojos?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                    {
                        "content": "¿Su hijo mira espontáneamente su rostro para ver su reacción cuando se enfrenta con algo poco familiar?",
                        "risk_type": "Frecuencia",
                        "risk_range": "Menos Frecuente",
                    },
                    {
                        "content": "¿Cuánto tiempo puede su hijo mantener el interés en sólo un objeto, o dos?",
                        "risk_type": "Temporal en un Día",
                        "risk_range": "Menos Tiempo",
                    },
                    {
                        "content": "¿Su hijo agita objetos repetidamente (p. ej. Trozos de cuerda)?",
                        "risk_type": "Tipicidad",
                        "risk_range": "Menos Típico",
                    },
                    {
                        "content": "¿Su hijo parece ser demasiado sensible al sonido?",
                        "risk_type": "Tipicidad",
                        "risk_range": "Menos Típico",
                    },
                    {
                        "content": "¿Su hijo se queda mirando al vacío sin objetivo aparente?",
                        "risk_type": "Frecuencia en Periodo",
                        "risk_range": "Menos Frecuente en un Periodo",
                    },
                ]

                for q in questions:
                    risk_type = TipoRiesgo.objects.get(nombre=q["risk_type"])

                    risk_range = RangoRiesgo.objects.get(rango=q["risk_range"], tipo_riesgo=risk_type)

                    QchatQuestion.objects.create(
                        content=q["content"],
                        risk_type=risk_type,
                        risk_range=risk_range,
                    )
                print("Preguntas de Q-Chat creado correctamente.")
                pass
        except (OperationalError, ProgrammingError):
            pass
