from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import CadastralQuery


class CadastralQueryViewTests(APITestCase):

    def setUp(self):
        self.valid_payload = {
            "cadastral_number": "77:01:0004010:1287",
            "latitude": 55.7558,
            "longitude": 37.6176,
        }
        self.query = CadastralQuery.objects.create(
            cadastral_number="77:01:0004010:1287",
            latitude=55.7558,
            longitude=37.6176,
            result=True,
        )

    def test_create_query(self):
        response = self.client.post(
            reverse("api:query"), self.valid_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CadastralQuery.objects.count(), 2)

    def test_get_result(self):
        response = self.client.get(reverse("api:result", kwargs={"pk": self.query.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["cadastral_number"], self.query.cadastral_number)

    def test_get_history(self):
        response = self.client.get(reverse("api:history"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_history_by_cadastral_number(self):
        response = self.client.get(
            reverse(
                "api:history_by_cadastral_number",
                kwargs={"cadastral_number": self.query.cadastral_number},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ping(self):
        response = self.client.get(reverse("api:ping"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "pong")
