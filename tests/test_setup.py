from rest_framework.test import APITestCase

from apps.base.models import TipoRiesgo, ValorRiesgo
from apps.mchatr.models import MchatRQuestions
from apps.patient.models import PatientData
from apps.qchat.models import QchatQuestion
from apps.qchat10.models import Qchat10Responses, Qchat10Question


class TestSetUp(APITestCase):
    BASE_URL = "http://127.0.0.1:8000/api/v2/"

    URLS = {
        # MCHATR
        "mchatr_questions": f"{BASE_URL}mchatr/mchat_questions/",
        "mchatr_response": f"{BASE_URL}mchatr/mchat_responses/",
        # QCHAT
        "qchat_questions": f"{BASE_URL}qchat/qchat_questions/",
        "qchat_response": f"{BASE_URL}qchat/qchat_responses/",
        # QCHAT10
        "qchat10_questions": f"{BASE_URL}qchat10/qchat10_questions/",
        "qchat10_response": f"{BASE_URL}qchat10/qchat10_responses/",
        # Dispatchers
        "dispatch_response": f"{BASE_URL}base/dispatch/dispatch_response/"
    }

    def setUp(self):
        from apps.user.models import UserProfile

        self.login_url = "/api/v2/token/"
        self.user = UserProfile.objects.create_superuser(
            username="superuser",
            email="superuser@admin.com",
            password="admin1234",
            first_name="develop",
            last_name="develop",
            phone_number="55075002"
        )

        response = self.client.post(self.login_url, {
            "username": self.user.username,
            "password": "admin1234"
        }, format="json")

        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)
        return super().setUp()

    def _get_data_response_qchat(self):
        from tests.data.qchat_questions import data_response

        import copy

        return copy.deepcopy(data_response)

    def _get_data_response_qchat10(self):
        from tests.data.qchat10_questions import data_response

        import copy

        return copy.deepcopy(data_response)

    def _get_data_response_mchatr(self):
        from tests.data.mchat_questions import data_response

        return data_response

    def _responses_with_high_risk(self, test):
        if test == "MCHATR":
            return self._get_data_response_mchatr()
        elif test == "QCHAT":
            data = self._get_data_response_qchat()

            for i in data:
                risk_type = TipoRiesgo.objects.get(nombre=i["risk_type"])

                risk_value = ValorRiesgo.objects.get(orden=4, tipo_riesgo=risk_type)

                i["response"] = risk_value.valor

            return data
        else:
            data = self._get_data_response_qchat10()

            for i in data:
                question = Qchat10Question.objects.get(id=i["id"])

                is_less_risk = question.risk_range.rango.startswith("Menos")

                risk_type = TipoRiesgo.objects.get(nombre=i["risk_type"])

                risk_value = ValorRiesgo.objects.get(orden=0 if is_less_risk else 4, tipo_riesgo=risk_type)

                i["response"] = risk_value.valor

            return data

    def _responses_with_low_risk(self, test):
        if test == "MCHATR":

            import copy
            from tests.data.mchat_questions import data_response
            data = copy.deepcopy(data_response)
            for i in data:
                question = MchatRQuestions.objects.get(id=i["id"])
                i["response"] = "NO" if question.response == "SI" else "SI"
            return data

        elif test == "QCHAT":
            data = self._get_data_response_qchat()

            for i in data:
                risk_type = TipoRiesgo.objects.get(nombre=i["risk_type"])

                risk_value = ValorRiesgo.objects.get(orden=0, tipo_riesgo=risk_type)

                i["response"] = risk_value.valor

            return data
        else:

            data = self._get_data_response_qchat10()

            for i in data:
                question = Qchat10Question.objects.get(id=i["id"])

                is_less_risk = question.risk_range.rango.startswith("Menos")

                risk_type = TipoRiesgo.objects.get(nombre=i["risk_type"])

                risk_value = ValorRiesgo.objects.get(orden=4 if is_less_risk else 0, tipo_riesgo=risk_type)

                i["response"] = risk_value.valor

            return data

    def _patient(self):
        return PatientData.objects.create(
            patient_name="paciente de prueba",
            CI="01062279905",
            age_in_month=24,
            tutor_name="tutor de prueba",
        )
