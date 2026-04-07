from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from .models import PatientData
from .serializers import PatientDataSerializers
from rest_framework import status
from rest_framework.response import Response


# Create your views here.
class PatientDataViewSet(ModelViewSet):
    queryset = PatientData.objects.all()

    serializer_class = PatientDataSerializers

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

        # Cambia "baseresponse" por el nombre real del modelo hijo
        lista = []
        responses_mchatr = getattr(patient, "mchatrresponses_responses", None)
        responses_qchat =  getattr(patient, "qchatresponses_responses", None)
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
            responses = [
                {
                    "created": r.created,
                    "puntuation": r.puntuation,
                    "responses": r.responses,
                    "valoration": getattr(r, "valoration", None),
                    "type": r.__class__.__name__
                }
                for r in all_responses
            ]
            return Response(responses, status=status.HTTP_200_OK)

        return Response(
            { "message": "No ha realizado pruebas" },
            status=status.HTTP_200_OK
        )
