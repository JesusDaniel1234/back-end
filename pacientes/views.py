from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import DatosPaciente
from .serializers import GestionarDatosPacientesSerializers
from rest_framework import status
from rest_framework.response import Response
from mchatr.serializers import DetallarRespuestasMChatRSimpSerializers
from qchat.serializers import DetallarRespuestasQChatSimpSerializers
from qchat10.serializers import DetallarRespuestasQChat10SimpSerializers


# Create your views here.
class DetallesDatosPacienteView(ModelViewSet):
    queryset = DatosPaciente.objects.all()
    serializer_class = GestionarDatosPacientesSerializers

    def create(self, request, *args, **kwargs):
        tarjeta_menor = request.data.get("tarjeta_menor")
        if DatosPaciente.objects.filter(tarjeta_menor=tarjeta_menor).exists():
            paciente_existente = DatosPaciente.objects.get(tarjeta_menor=tarjeta_menor)
            paciente_serializado = self.serializer_class(paciente_existente).data
            return Response({"error": "El paciente ya existe", "data": paciente_serializado},status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class DetallesPacienteYRespuestasView(APIView):
    def get(self,request, pk):
        paciente = DatosPaciente.objects.filter(id=pk).first()
        serializers_paciente = GestionarDatosPacientesSerializers(paciente)
        tests = ["MChatR", "QChat", "QChat10"]
        
        serializers_dict = {
            "MChatR":DetallarRespuestasMChatRSimpSerializers,
            "QChat":DetallarRespuestasQChatSimpSerializers,
            "QChat10":DetallarRespuestasQChat10SimpSerializers,
        }
        
        if paciente:
            testMchatr = paciente.respuestasmchtr_set.first()
            testQChat = paciente.respuestasqchat_set.first()
            testQChat10 = paciente.respuestasqchat10_set.first()

            paciente_dict = {
            "MChatR":testMchatr,
            "QChat":testQChat,
            "QChat10":testQChat10,
            }
            
            lista_tests = []
            for test in tests:
                if paciente_dict[test] is not None:
                    lista_tests.append({"tipo":test,"respuesta": serializers_dict[test](paciente_dict[test]).data})

            return Response({"paciente":serializers_paciente.data, "tests":lista_tests }, status=status.HTTP_200_OK)
        return Response({"error":"El paciente no existe"}, status=status.HTTP_404_NOT_FOUND)
