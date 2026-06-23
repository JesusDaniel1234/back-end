from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .filters import PatientFilter
from .models import PatientData
from .serializers import PatientDataSerializers
from rest_framework import status
from rest_framework.response import Response

from ..base.pagination import MediumPaginationClass, SmallPaginationClass


# Create your views here.
class PatientDataViewSet(ModelViewSet):
    queryset = PatientData.objects.all().order_by("id")
    filter_backends = [SearchFilter, DjangoFilterBackend]
    serializer_class = PatientDataSerializers
    pagination_class = MediumPaginationClass
    filterset_class = PatientFilter

    search_fields = [
        "patient_name",
        "tutor_name",
        "CI",
    ]

    def create(self, request, *args, **kwargs):
        ci = request.data.get("CI")

        if PatientData.objects.filter(ci=ci).exists():
            patient = PatientData.objects.get(ci=ci)

            serializer = self.serializer_class(patient)

            return Response({ "error": "El paciente ya existe", "data": serializer.data }, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)

            serializer.is_valid(raise_exception=True)

            self.perform_create(serializer)

            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=["get"], detail=True)
    def get_responses(self, request, pk=None):
        from itertools import chain
        patient = self.get_object()

        responses_mchatr = getattr(patient, "mchatrresponses_responses", None)
        responses_qchat = getattr(patient, "qchatresponses_responses", None)
        responses_qchat10 = getattr(patient, "qchat10responses_responses", None)

        querysets = [
            qs.all() for qs in [
                responses_mchatr,
                responses_qchat,
                responses_qchat10
            ] if qs is not None
        ]

        all_responses = list(chain(*querysets))
        if all_responses:
            responses = []
            for r in all_responses:
                type_class = r.__class__.__name__.lower()
                test = "MCHATR" if type_class.startswith("mchatr") else "QCHAT10" if type_class.startswith(
                    "qchat10") else "QCHAT"
                responses.append(
                    {
                        "created": r.created,
                        "puntuation": r.puntuation,
                        "id": r.id,
                        "valoration": getattr(r, "valoration", None),
                        "test": test,
                        "class": r.__class__.__name__
                    }

                )
            return Response(responses, status=status.HTTP_200_OK)

        return Response(
            { "message": "No ha realizado pruebas" },
            status=status.HTTP_200_OK
        )
