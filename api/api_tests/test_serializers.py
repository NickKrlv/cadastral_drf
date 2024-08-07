from django.test import TestCase
from api.serializers import CadastralQuerySerializer
from api.models import CadastralQuery


class CadastralQuerySerializerTest(TestCase):

    def setUp(self):
        self.query_data = {
            "cadastral_number": "77:01:0004010:1287",
            "latitude": 55.7558,
            "longitude": 37.6176,
        }
        self.query = CadastralQuery.objects.create(**self.query_data, result=True)
        self.serializer = CadastralQuerySerializer(instance=self.query)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(
            data.keys(),
            ["id", "cadastral_number", "latitude", "longitude", "result", "timestamp"],
        )

    def test_query_content(self):
        data = self.serializer.data
        self.assertEqual(data["cadastral_number"], self.query_data["cadastral_number"])
        self.assertEqual(data["latitude"], self.query_data["latitude"])
        self.assertEqual(data["longitude"], self.query_data["longitude"])
        self.assertEqual(data["result"], True)
