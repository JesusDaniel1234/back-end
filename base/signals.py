from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import TipoRiesgo, RangoRiesgo, ValorRiesgo


@receiver(post_migrate)
def insert_initial_data(sender, **kwargs):
    if sender.name == "base":
        if not TipoRiesgo.objects.exists():
            tipos_riesgo = [
                "Temporal en un Día",
                "Cantidad de Palabras",
                "Temporal",
                "Frecuencia en Periodo",
                "Tipicidad",
                "Facilidad",
                "Frecuencia",
            ]
            for tipo in tipos_riesgo:
                TipoRiesgo.objects.create(nombre=tipo)

        if not RangoRiesgo.objects.exists():
            rango_riesgo = [
                ["Más Tiempo", "Menos Tiempo", "Temporal en un Día"],
                [
                    "Mayor Número de Palabras",
                    "Menor Número de Palabras",
                    "Cantidad de Palabras",
                ],
                ["Más Tiempo", "Menos Tiempo", "Temporal"],
                [
                    "Más Frecuente en un Periodo",
                    "Menos Frecuente en un Periodo",
                    "Frecuencia en Periodo",
                ],
                ["Más Típico", "Menos Típico", "Tipicidad"],
                ["Más Fácil", "Menos Fácil", "Facilidad"],
                ["Más Frecuente", "Menos Frecuente", "Frecuencia"],
            ]

            for rango in rango_riesgo:
                tipo = TipoRiesgo.objects.get(nombre=rango[-1])
                for i in range(len(rango) - 1):
                    RangoRiesgo.objects.create(rango=rango[i], tipo_riesgo=tipo)

        if not ValorRiesgo.objects.exists():
            valor_riesgo = [
                {
                    "tipos_riesgo": "Frecuencia",
                    "valor_riesgo": [
                        "Nunca",
                        "Rara Vez",
                        "A Veces",
                        "Usualmente",
                        "Siempre",
                    ],
                },
                {
                    "tipos_riesgo": "Facilidad",
                    "valor_riesgo": [
                        "Imposible",
                        "Muy Difícil",
                        "Difícil",
                        "Bastante Fácil",
                        "Muy Fácil",
                    ],
                },
                {
                    "tipos_riesgo": "Tipicidad",
                    "valor_riesgo": [
                        "No lo Hace",
                        "Muy Inusual",
                        "Inusual",
                        "Bastante Típico",
                        "Muy Típico",
                    ],
                },
                {
                    "tipos_riesgo": "Frecuencia en Periodo",
                    "valor_riesgo": [
                        "Nunca",
                        "Más de una vez a la Semana",
                        "Algunas Veces a la Semana",
                        "Algunas Veces en un Día",
                        "Muchas Veces en un Día",
                    ],
                },
                {
                    "tipos_riesgo": "Temporal",
                    "valor_riesgo": [
                        "Menos de un Minuto",
                        "Par de Minutos",
                        "10 Minutos",
                        "Media Hora",
                        "Varias Horas",
                    ],
                },
                {
                    "tipos_riesgo": "Cantidad de Palabras",
                    "valor_riesgo": [
                        "No ha comenzado a hablar",
                        "Menos de 10 palabras",
                        "Entre 10 y 50 palabras",
                        "Entre 50 y 100 palabras",
                        "Más de 100 palabras",
                    ],
                },
                {
                    "tipos_riesgo": "Temporal en un Día",
                    "valor_riesgo": [
                        "Un par de minutos",
                        "10 Minutos",
                        "Media Hora",
                        "Varias Horas",
                        "Gran Parte del día",
                    ],
                },
            ]

            for valor in valor_riesgo:
                tipo = TipoRiesgo.objects.get(nombre=valor["tipos_riesgo"])
                for i in range(len(valor["valor_riesgo"])):
                    ValorRiesgo.objects.create(
                        valor=valor["valor_riesgo"][i], orden=i, tipo_riesgo=tipo
                    )
