from django.db import models


class CadastralQuery(models.Model):
    cadastral_number = models.CharField(max_length=255, verbose_name="Cadastral number")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    result = models.BooleanField(null=True, blank=True, verbose_name="Result")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")

    def __str__(self):
        return f"{self.cadastral_number} at {self.timestamp}"
