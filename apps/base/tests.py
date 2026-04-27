from apps.base.models import TipoRiesgo, ValorRiesgo
from apps.mchatr.models import MchatRQuestions
from apps.qchat.models import QchatQuestion
from apps.qchat10.models import Qchat10Question
from tests.test_setup import TestSetUp


class TestsDispatchResponse(TestSetUp):
    def get_url(self):
        return self.URLS["dispatch_response"]

    def test_integration_mchatr(self):
        """
            Prueba de Integración (Respuesta de pruebas mediante el endpoint Dispatch)
            Obtención de resultados mediante endpointDispatch
        """
        test = "MCHATR"

        patient = self._patient()
        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_high_risk(test)
        }

        response = self.client.post(f"{self.get_url()}?test={test}", data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Respuesta almacenada correctamente")

        response = self.client.get(f"{self.get_url()}?test={test}&id={patient.id}", format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["puntuation"], 20)
        self.assertEqual(response.data["valoration"], "AR")

    def test_integration_qchat(self):
        """
            Prueba de Integración (Respuesta de pruebas mediante el endpoint Dispatch)
            Obtención de resultados mediante endpointDispatch
        """
        test = "QCHAT"

        patient = self._patient()
        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_high_risk(test)
        }

        response = self.client.post(f"{self.get_url()}?test={test}", data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Respuesta almacenada correctamente")

        response = self.client.get(f"{self.get_url()}?test={test}&id={patient.id}", format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["puntuation"], 100)
        self.assertEqual(response.data["valoration"], "AR")

    def test_integration_qchat10(self):
        """
            Prueba de Integración (Respuesta de pruebas mediante el endpoint Dispatch)
            Obtención de resultados mediante endpointDispatch
        """
        test = "QCHAT10"
        patient = self._patient()

        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_high_risk(test)
        }

        response = self.client.post(f"{self.get_url()}?test={test}", data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Respuesta almacenada correctamente")

        response = self.client.get(f"{self.get_url()}?test={test}&id={patient.id}", format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["puntuation"], 10)
        self.assertEqual(response.data["valoration"], "AR")


class TestStats(TestSetUp):
    URL_RESPONSE = "http://127.0.0.1:8000/api/v2/base/dispatch/dispatch_response/"
    URL_STATS = "http://127.0.0.1:8000/api/v2/base/stats/mchatr_responses_stats/"

    def test_integration_mchatr(self):
        test = "MCHATR"

        patient = self._patient()
        data = {
            "patient_name": patient.patient_name,
            "CI": patient.CI,
            "age_in_month": patient.age_in_month,
            "tutor_name": patient.tutor_name,
            "responses": self._responses_with_high_risk(test)
        }

        response = self.client.post(f"{self.URL_RESPONSE}?test={test}", data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Respuesta almacenada correctamente")

        response = self.client.get(f"{self.URL_STATS}", data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total"], 1)
        self.assertEqual(response.data["avg_score"], float(20))
