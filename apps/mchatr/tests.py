from apps.mchatr.models import MchatRQuestions
from apps.patient.models import PatientData
from tests.test_setup import TestSetUp


# Create your tests here.
class TestMchatRQuestions(TestSetUp):
    URL = "http://localhost:8000/api/v1/mchatr/mchat_questions/"

    def _question(self):
        return MchatRQuestions.objects.create(
            content="Nueva pregunta",
            response="NO",
            created_by=self.user,
            is_active=True
        )

    def test_list_questions_by_url(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 20)

    def test_create_question_by_url(self):
        data = { "content": "nueva preguta", "response": "NO", "created_by": self.user.id, "is_active": True }

        response = self.client.post(self.URL, data, frmat="json")
        self.assertEqual(response.status_code, 201)
        # Ya existen 20 preguntas creadas así que la nueva estará con el id 21
        self.assertEqual(response.data["id"], 21)

    def test_updated_question_by_url(self):
        # Crear pregunta:
        created = self._question()

        # Actualizar pregunta
        update_data = { "is_active": False, "content": "pregunta actualizada", "response": "SI" }
        response = self.client.patch(f"{self.URL}{created.id}/", update_data, frmat="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], update_data["content"])

    def test_delete_question_by_url(self):
        # Crear pregunta:
        created = self._question()

        # Eliminar Pregunta
        response = self.client.delete(f"{self.URL}{created.id}/")

        self.assertEqual(response.status_code, 204)


class TestMChatRResponses(TestSetUp):
    URL = "http://localhost:8000/api/v1/mchatr/mchat_responses/"

    def _patient(self):
        return PatientData.objects.create(
            patient_name="paciente de prueba",
            CI="01062279905",
            age_in_month=24,
            tutor_name="tutor de prueba",
        )

    def _default_responses(self):
        from tests.data.mchat_questions import data_response
        return data_response

    def _responses_with_reverse_response(self):
        import copy
        from tests.data.mchat_questions import data_response
        data = copy.deepcopy(data_response)
        for i in data:
            question = MchatRQuestions.objects.get(id=i["id"])
            i["response"] = "NO" if question.response == "SI" else "SI"
        return data

    def test_high_risk_case(self):
        """
            Prueba de Integración
            - con la función __responses_with_reverse_response, todas las respuestas están en estado
            de riesgo.
            - con esto la puntuación obtenida debe ser la máxima
        """
        patient = self._patient()
        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._default_responses()
        }

        response = self.client.post(self.URL, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["puntuation"], 20)
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
            "responses": self._responses_with_reverse_response()
        }

        response = self.client.post(self.URL, data, format="json")

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
            "responses": self._responses_with_reverse_response()[:10]
        }

        response = self.client.post(self.URL, data, format="json")

        # Error 400 La cantidad de respuestas no coincide con la cantidad de preguntas activas
        self.assertEqual(response.status_code, 400)
