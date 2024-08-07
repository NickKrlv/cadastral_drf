from django.test import TestCase
from api.models import CadastralQuery


class CadastralQueryModelTest(TestCase):

    def setUp(self):
        self.query = CadastralQuery.objects.create(
            cadastral_number="77:01:0004010:1287",
            latitude=55.7558,
            longitude=37.6176,
            result=True,
        )

    def test_query_creation(self):
        self.assertIsInstance(self.query, CadastralQuery)
        self.assertEqual(self.query.cadastral_number, "77:01:0004010:1287")
        self.assertEqual(self.query.latitude, 55.7558)
        self.assertEqual(self.query.longitude, 37.6176)
        self.assertEqual(self.query.result, True)
