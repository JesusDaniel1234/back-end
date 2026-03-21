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
