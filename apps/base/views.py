from rest_framework.decorators import action
from rest_framework.generics import (
    ListAPIView, get_object_or_404,
)
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from .models import (
    # Q-chat-100
    TipoRiesgo,
    ValorRiesgo,
    RangoRiesgo,
)
from apps.user.models import UserProfile
from .serializers import (
    # Q-chat-100
    TipoRiesgoSerializers,
    ValorRiesgoSerializers,
    RangoRiesgoSerializers,
)
from apps.patient.models import PatientData
from django.db.models import Sum, Count, Avg
from rest_framework.response import Response
from rest_framework import status

# Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..mchatr.models import MchatRQuestions, MChatRResponses
from ..mchatr.serializers import MchatRQuestionsSerializers, MChatRResponsesSerializers
from ..qchat.models import QchatQuestion, QchatResponses
from ..qchat.serializers import QChatQuestionSerializers, QChatResponseSerializers
from ..qchat10.models import Qchat10Question, Qchat10Responses
from ..qchat10.serializers import QChat10QuestionSerializers, QChat10ResponseSerializers


# Token configuration
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        token["is_staff"] = user.is_staff
        token["is_superuser"] = user.is_superuser

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Despachador de Pruebas
class DispatchTestsViewSet(ViewSet):
    TEST_MAP = {
        "MCHATR": (MchatRQuestions, MchatRQuestionsSerializers),
        "QCHAT": (QchatQuestion, QChatQuestionSerializers),
        "QCHAT10": (Qchat10Question, QChat10QuestionSerializers),
    }

    RESPONSE_MAP = {
        "MCHATR": (MChatRResponses, MChatRResponsesSerializers),
        "QCHAT": (QchatResponses, QChatResponseSerializers),
        "QCHAT10": (Qchat10Responses, QChat10ResponseSerializers),
    }

    @action(methods=["get"], detail=False)
    def dispatch_questions(self, request):
        test = request.query_params.get("test")

        if test not in self.TEST_MAP:
            return Response({ "error": f"Prueba {test} no encontrada" }, status=status.HTTP_404_NOT_FOUND)

        model, serializer_class = self.TEST_MAP[test]
        queryset = model.objects.filter(is_active=True)
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post", "get"], detail=False)
    def dispatch_response(self, request, *args, **kwargs):
        test = request.query_params.get("test")

        if test not in self.RESPONSE_MAP:
            return Response({ "error": f"Prueba {test} no encontrada" }, status=status.HTTP_404_NOT_FOUND)

        model, serializer_class = self.RESPONSE_MAP[test]

        if request.method == "POST":
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({ "message": "Respuesta almacenada correctamente" }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            id = request.query_params.get("id")
            if not id:
                return Response({ "error": f"Falta el id de la respuesta" }, status=status.HTTP_400_BAD_REQUEST)

            instance = get_object_or_404(model, id=id)
            serializer = serializer_class(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False)
    def dispatch_stats(self, request, *args, **kwargs):
        import numpy as np
        test = request.query_params.get("test")

        if test not in self.RESPONSE_MAP:
            return Response({ "error": f"Prueba {test} no encontrada" }, status=status.HTTP_404_NOT_FOUND)

        model, serializer_class = self.RESPONSE_MAP[test]
        queryset = model.objects.all()

        # cantidad
        total = queryset.count()
        # Media
        avg_score = queryset.aggregate(avg=Avg("puntuation"))["avg"]

        low = queryset.filter(puntuation__lte=2).count()
        moderate = queryset.filter(puntuation__gte=3, puntuation__lte=7).count()
        high = queryset.filter(puntuation__gte=8).count()

        puntuations = list(queryset.values_list('puntuation', flat=True))

        if not puntuations:
            return Response({
                "total": 0,
                "avg_score": 0,
                "min_score": 0,
                "max_score": 0,
                "distribution": {
                    "low": 0,
                    "moderate": 0,
                    "high": 0
                },
                "screening_positive_rate": 0,
                "percentages": {
                    "low": 0,
                    "moderate": 0,
                    "high": 0,
                },
                "percentiles": {
                    "p25": 0,
                    "p50": 0,
                    "p75": 0,
                }
            }, status=status.HTTP_200_OK)

        return Response({
            "total": total,
            "avg_score": round(avg_score or 0, 1),
            "min_score": min(puntuations),
            "max_score": max(puntuations),
            "distribution": {
                "low": low,
                "moderate": moderate,
                "high": high
            },
            "screening_positive_rate": round((moderate + high) / total * 100, 1) if total else 0,
            "percentages": {
                "low": round(low / total * 100 if total else 0, 1),
                "moderate": round(moderate / total * 100 if total else 0, 1),
                "high": round(high / total * 100 if total else 0, 1),
            },
            "percentiles": {
                "p25": np.percentile(puntuations, 25),
                "p50": np.percentile(puntuations, 50),
                "p75": np.percentile(puntuations, 75),
            }
        }, status=status.HTTP_200_OK)

# El servidor funciona
class ActiveServerView(APIView):
    def get(self, request):
        return Response({ "message": "OK" }, status=status.HTTP_200_OK)


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
