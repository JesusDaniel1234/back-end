from django.db.models.signals import post_migrate
from .models import Qchat10Question
from apps.base.models import RangoRiesgo, TipoRiesgo, ValorRiesgo
from django.dispatch import receiver


@receiver(post_migrate)
def create_questions_qchat(sender, **kwargs):
    if sender.name == "apps.qchat10":

        if not Qchat10Question.objects.exists():

            preguntas = [
                {
                    "content": "¿Su niño/a lo/a mira a usted cuando lo llama por su nombre?",
                    "risk_type": "Frecuencia",
                    "risk_value": "A Veces",
                    "risk_range": "Menos Frecuente",
                },
                {
                    "content": "¿Su niño/a sigue su mirada hacia donde usted está mirando?",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "Algunas Veces a la Semana",
                    "risk_range": "Menos Frecuente en un Periodo",
                },
                {
                    "content": "¿Su niño/a le mira espontáneamente a la cara para ver su reacción, cuando ocurre algo que no es habitual?",
                    "risk_type": "Frecuencia",
                    "risk_value": "A Veces",
                    "risk_range": "Menos Frecuente",
                },
                {
                    "content": "Si usted o alguien en su familia está visiblemente angustiado o triste, ¿Su niño/a muestra signos de querer ayudarlo?. Por ejemplo, acariciando su pelo o abrazándolo",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "A Veces",
                    "risk_range": "Menos Frecuente en un Periodo",
                },
                {
                    "content": "¿Su niño/a utiliza gestos simples?. Por ejemplo, cuando se despide, ¿hace como “chao”?",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "Algunas Veces a la Semana",
                    "risk_range": "Menos Frecuente en un Periodo",
                },
                {
                    "content": "¿Que tan fácil es para usted tener contacto visual con su niño/a?. Por ejemplo, que el/ella le mire.",
                    "risk_type": "Facilidad",
                    "risk_value": "Difícil",
                    "risk_range": "Menos Fácil",
                },
                {
                    "content": "¿Su niño/a apunta con el dedo cuando quiere algo? Por ejemplo, un juguete que está fuera de su alcance.",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "Algunas Veces a la Semana",
                    "risk_range": "Menos Frecuente en un Periodo",
                },
                {
                    "content": "¿Su niño/a juega a simular?. Por ejemplo, hacer “como si” cuidara su muñeca o “como si” hablara por un teléfono de juguete.",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "Algunas Veces a la Semana",
                    "risk_range": "Menos Frecuente en un Periodo",
                },
                {
                    "content": "¿Su niño/a apunta con el dedo para mostrarle algo que le interesa? Por ejemplo, apunta para mostrarle o compartir algo interesante.",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "Algunas Veces a la Semana",
                    "risk_range": "Menos Frecuente en un Periodo",
                },
                {
                    "content": "¿Tu niño/a mira a la nada, como sin propósito aparente?. Por ejemplo, mirando un punto fijo.",
                    "risk_type": "Frecuencia en Periodo",
                    "risk_value": "Algunas Veces a la Semana",
                    "risk_range": "Más Frecuente en un Periodo",
                },

            ]

            for pregunta in preguntas:
                risk_type = TipoRiesgo.objects.get(nombre=pregunta["risk_type"])

                risk_range = RangoRiesgo.objects.get(rango=pregunta["risk_range"])

                risk_value = ValorRiesgo.objects.get(valor=pregunta["risk_value"])

                Qchat10Question.objects.create(
                    content=pregunta["content"],
                    risk_type=risk_type,
                    risk_range=risk_range,
                    risk_value=risk_value
                )

            print("Preguntas de Q-Chat-10 creado correctamente.")
