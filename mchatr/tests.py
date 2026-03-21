from tests.test_setup import TestSetUp


# Create your tests here.
class TestMchatRQuestions(TestSetUp):
    URL = "http://localhost:8000/api/v1/mchatr/mchat_questions/"

    def test_list_questions_by_url(self):
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 20)

    def test_create_question_by_url(self):
        data = { "content": "nueva preguta", "response": "NO", "created_by": self.user.id, "is_activa": True }

        response = self.client.post(self.URL, data, frmat="json")
        self.assertEqual(response.status_code, 201)
        # Ya existen 20 preguntas creadas así que la nueva estará con el id 21
        self.assertEqual(response.data["id"], 21)

    def test_updated_question_by_url(self):
        # Crear pregunta:
        data = { "content": "nueva preguta", "response": "NO", "created_by": self.user.id, "is_activa": True }
        created = self.client.post(self.URL, data, frmat="json")

        # Actualizar pregunta
        update_data = { "is_activa": False, "content": "pregunta actualizada", "response": "SI" }
        response = self.client.patch(f"{self.URL}{created.data["id"]}/", update_data, frmat="json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], update_data["content"])

    def test_delete_question_by_url(self):
        # Crear pregunta:
        data = { "content": "nueva preguta", "response": "NO", "created_by": self.user.id, "is_activa": True }
        created = self.client.post(self.URL, data, frmat="json")

        # Eliminar Pregunta
        response = self.client.delete(f"{self.URL}{created.data["id"]}/")

        self.assertEqual(response.status_code, 204)


class TestMChatRResponses(TestSetUp):
    pass
