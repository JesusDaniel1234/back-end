from apps.qchat.models import QchatQuestion
from apps.patient.models import PatientData
from apps.base.models import TipoRiesgo, RangoRiesgo, ValorRiesgo
from tests.test_setup import TestSetUp


# Create your tests here.
class TestQchatQuestions(TestSetUp):
    def get_url(self):
        return self.URLS["qchat_questions"]

    def _question(self):
        risk_type = TipoRiesgo.objects.get(nombre="Frecuencia")

        risk_range = RangoRiesgo.objects.get(rango="Menos Frecuente", tipo_riesgo=risk_type)

        return QchatQuestion.objects.create(
            content="Nueva pregunta",
            risk_type=risk_type,
            risk_range=risk_range,
            created_by=self.user,
            is_active=True
        )

    def test_list_questions_by_url(self):
        response = self.client.get(self.get_url())

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data), 25)

    def test_create_question_by_url(self):
        risk_type = TipoRiesgo.objects.get(nombre="Frecuencia")

        risk_range = RangoRiesgo.objects.get(rango="Menos Frecuente", tipo_riesgo=risk_type)

        data = {
            "content": "nueva preguta",
            "risk_type": risk_type.id,
            "risk_range": risk_range.id,
            "created_by": self.user.id,
            "is_active": True
        }

        response = self.client.post(self.get_url(), data, frmat="json")

        self.assertEqual(response.status_code, 201)
        # Ya existen 26 preguntas creadas así que la nueva estará con el id 26
        self.assertEqual(response.data["id"], 26)

    def test_updated_question_by_url(self):
        # Crear pregunta:
        created = self._question()

        # Actualizar pregunta
        risk_type = TipoRiesgo.objects.get(nombre="Tipicidad")

        risk_range = RangoRiesgo.objects.get(rango="Menos Típico", tipo_riesgo=risk_type)

        update_data = {
            "is_active": False,
            "content": "pregunta actualizada",
            "risk_type": risk_type.id,
            "risk_range": risk_range.id
        }

        response = self.client.patch(f"{self.get_url()}{created.id}/", update_data, frmat="json")

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["content"], update_data["content"])

    def test_delete_question_by_url(self):
        # Crear pregunta:
        created = self._question()

        # Eliminar Pregunta
        response = self.client.delete(f"{self.get_url()}{created.id}/")

        self.assertEqual(response.status_code, 204)


class TestQChatResponses(TestSetUp):
    def get_url(self):
        return self.URLS["qchat_response"]

    def test_high_risk_case(self):
        """
            Prueba de Integración
            - con la función _responses_with_high_risk, todas las respuestas están en estado
            de riesgo.
            - con esto la puntuación obtenida debe ser la máxima
        """
        patient = self._patient()

        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_high_risk("QCHAT")
        }

        response = self.client.post(self.get_url(), data, format="json")

        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.data["puntuation"], 100)

        self.assertEqual(response.data["valoration"], "AR")

    def test_low_risk_case(self):
        """
            Prueba de Integración
            - con la función _default_responses, todas las respuestas presentan el mismo estado.
            - con esto la puntuación obtenida debe ser 0
        """
        patient = self._patient()

        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_low_risk("QCHAT")
        }

        response = self.client.post(self.get_url(), data, format="json")

        self.assertEqual(response.status_code, 201)

        self.assertEqual(response.data["puntuation"], 0)

        self.assertEqual(response.data["valoration"], "BR")

    def test_validate_response_number(self):

        patient = self._patient()

        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_high_risk("QCHAT")[:10]
        }

        response = self.client.post(self.get_url(), data, format="json")

        # Error 400 La cantidad de respuestas no coincide con la cantidad de preguntas activas
        self.assertEqual(response.status_code, 400)
