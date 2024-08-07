from rest_framework import serializers
from .models import CadastralQuery


class CadastralQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastralQuery
        fields = "__all__"
