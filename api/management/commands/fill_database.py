import random
from django.core.management.base import BaseCommand
from api.models import CadastralQuery


class Command(BaseCommand):
    help = "Fill the database"

    def handle(self, *args, **kwargs):

        cadastral_numbers = [
            "77:01:0004010:1287",
            "77:01:0004010:1288",
            "77:01:0004010:1289",
            "77:01:0004010:1290",
            "77:01:0004010:1291",
            "77:01:0004010:1292",
            "77:01:0004010:1293",
            "77:01:0004010:1294",
            "77:01:0004010:1295",
            "77:01:0004010:1296",
        ]
        latitudes = [
            55.7558,
            55.7560,
            55.7562,
            55.7564,
            55.7566,
            55.7568,
            55.7570,
            55.7572,
            55.7574,
            55.7576,
        ]
        longitudes = [
            37.6176,
            37.6178,
            37.6180,
            37.6182,
            37.6184,
            37.6186,
            37.6188,
            37.6190,
            37.6192,
            37.6194,
        ]

        for i in range(10):
            cadastral_number = random.choice(cadastral_numbers)
            latitude = random.choice(latitudes)
            longitude = random.choice(longitudes)

            CadastralQuery.objects.get_or_create(
                cadastral_number=cadastral_number,
                latitude=latitude,
                longitude=longitude,
            )

        self.stdout.write(self.style.SUCCESS("Successfully filled the database"))
