from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.views import APIView
from .models import (
    # Q-chat-100
    TipoRiesgo,
    ValorRiesgo,
    RangoRiesgo,
)
from user.models import PerfilUsuario
from .serializers import (
    # Q-chat-100
    TipoRiesgoSerializers,
    ValorRiesgoSerializers,
    RangoRiesgoSerializers,
)
from pacientes.models import DatosPaciente
from django.db.models import Avg, Sum, Count
from rest_framework.response import Response
from rest_framework import status

# Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def valordefinidoPorPuntuacion(test, puntuacion):
    print(test, puntuacion)
    valorPorPuntuacion = {
        "mchatr": "AR" if puntuacion > 7 else "MR" if puntuacion > 2 else "BR" if puntuacion
        > 1  else "NR",
        "qchat": "AR" if puntuacion > 51.8 else "MR" if puntuacion > 26.7 else "BR" if puntuacion
        > 1  else "NR",
        "qchat10": "AR" if puntuacion > 3 else "BR" if puntuacion
        > 1  else "NR",
    }
    
    return valorPorPuntuacion[test]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        perfil = PerfilUsuario.objects.get(usuario=user)
        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email
        token["id_perfil"] = perfil.id
        token["id_usuario"] = user.id
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# base
class ListarTipoRiesgoView(ListAPIView):
    queryset = TipoRiesgo.objects.all()
    serializer_class = TipoRiesgoSerializers  


class ListarRangoRiesgoView(ListAPIView):
    queryset = RangoRiesgo.objects.all()
    serializer_class = RangoRiesgoSerializers


class ListarValorRiesgoView(ListAPIView):
    queryset = ValorRiesgo.objects.all()
    serializer_class = ValorRiesgoSerializers

def calcularValorRiesgo(mchatr,qchat,qchat10):
    resultados = [mchatr, qchat, qchat10]
    # Lógica de prioridad
    if "AR" in resultados:
        return "AR"  # Si al menos uno es AR
    elif "MR" in resultados:
        return "MR"  # Si al menos uno es MR (y ninguno es AR)
    elif all(r == "BR" for r in resultados):
        return "BR"  # Si todos son BR
    
calcularValorRiesgo("BR","BR","BR")
    
def calcularRiesgo(paciente):
    # Usar agregaciones para calcular suma y conteo en una sola consulta
    qchat10_agg = paciente.respuestasqchat10_set.aggregate(
        suma=Sum('puntuacion'), count=Count('puntuacion')
    )
    qchat_agg = paciente.respuestasqchat_set.aggregate(
        suma=Sum('puntuacion'), count=Count('puntuacion')
    )
    mchatr_agg = paciente.respuestasmchtr_set.aggregate(
        suma=Sum('puntuacion'), count=Count('puntuacion')
    )

    # Calcular los promedios manejando casos de listas vacías
    respuesta_qchat10 = qchat10_agg['suma'] / qchat10_agg['count'] if qchat10_agg['count'] > 0 else 0
    respuesta_qchat = qchat_agg['suma'] / qchat_agg['count'] if qchat_agg['count'] > 0 else 0
    respuesta_mchatr = mchatr_agg['suma'] / mchatr_agg['count'] if mchatr_agg['count'] > 0 else 0
    print("Estras son las respuestas:",respuesta_qchat10, respuesta_qchat, respuesta_mchatr)
    # Calcular el riesgo
    lista_resultados = [0 if respuesta_mchatr < 3 else 1, 0 if respuesta_qchat10 < 3 else 1, 0 if respuesta_qchat < 51 else 1]
    riesgo = int((sum(lista_resultados)/(len(lista_resultados)))*100)

    valor_qchat10 = valordefinidoPorPuntuacion("qchat10", respuesta_qchat10 )
    valor_qchat = valordefinidoPorPuntuacion("qchat", respuesta_qchat )
    valor_mchatr = valordefinidoPorPuntuacion("mchatr", respuesta_mchatr )
    
    riesgo = calcularValorRiesgo(valor_qchat10,
valor_qchat,
valor_mchatr)
    
    return [valor_qchat10,valor_qchat ,valor_mchatr , riesgo]

class ListaResultadosGeneralesPorPaciente(APIView):
    def get(self, request):
        pacientes = DatosPaciente.objects.all()
        # Crear una lista para almacenar los resultados
        resultado = []

        # Recorrer cada paciente y obtener las puntuaciones de las pruebas
        for paciente in pacientes:
            valor_qchat10, valor_qchat, valor_mchatr, riesgo = calcularRiesgo(paciente)
            datos_paciente = {
                'nombre_paciente': paciente.nombre_paciente,
                "tutor": paciente.nombre_tutor,
                "edad_meses": paciente.edad_paciente_meses,
                'respuestas_qchat10': valor_qchat10,
                'respuestas_qchat': valor_qchat,
                'respuestas_mchtr': valor_mchatr,
                "riesgo": riesgo,
                "id": paciente.id
            }
            resultado.append(datos_paciente)
        
        return Response(resultado, status=status.HTTP_200_OK)

class ServidorActivoView(APIView):
    def get(self, request):
        return Response({"message":"OK"}, status=status.HTTP_200_OK)