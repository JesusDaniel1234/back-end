import django_filters
from django.db.models import Q
from .models import PatientData


class PatientFilter(django_filters.FilterSet):
    test = django_filters.CharFilter(method="filter_test")
    valoration = django_filters.CharFilter(method="filter_test")

    class Meta:
        model = PatientData
        fields = []

    def filter_test(self, queryset, name, value):
        test = self.data.get("test")
        valoration = self.data.get("valoration")

        rules = {
            "MCHATR": {
                "relation": "mchatrresponses_responses",
                "BR": { "puntuation__lt": 3 },
                "MR": {
                    "puntuation__gte": 3,
                    "puntuation__lte": 7,
                },
                "AR": { "puntuation__gt": 7 },
            },
            "QCHAT": {
                "relation": "qchatresponses_responses",
                "BR": { "puntuation__lte": 26.7 },
                "MR": {
                    "puntuation__gt": 26.7,
                    "puntuation__lte": 51.8,
                },
                "AR": { "puntuation__gt": 51.8 },
            },
            "QCHAT10": {
                "relation": "qchat10responses_responses",
                "BR": { "puntuation__lte": 3 },
                "AR": { "puntuation__gt": 3 },
            },
        }

        if test == "GENERAL":
            if valoration:
                # filtra por property valoration del paciente
                return queryset.filter().distinct().filter(
                    pk__in=[
                        p.pk for p in queryset
                        if p.valoration == valoration
                    ]
                )

            # si no hay valoration → todos los pacientes
            return queryset

        # Sin filtros
        if not test and not valoration:
            return queryset

        if test and valoration:
            config = rules.get(test)
            if not config or valoration not in config:
                return queryset.none()

            relation = config["relation"]

            query = {
                f"{relation}__{k}": v
                for k, v in config[valoration].items()
            }

            return queryset.filter(**query).distinct()

        if test:
            config = rules.get(test)
            if not config:
                return queryset.none()

            relation = config["relation"]

            return queryset.filter(
                **{ f"{relation}__isnull": False }
            ).distinct()

        if valoration:
            q = Q()

            for config in rules.values():
                if valoration not in config:
                    continue

                relation = config["relation"]

                conditions = {
                    f"{relation}__{k}": v
                    for k, v in config[valoration].items()
                }

                q |= Q(**conditions)

            return queryset.filter(q).distinct()

        return queryset

