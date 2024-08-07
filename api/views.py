from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CadastralQuery
from .serializers import CadastralQuerySerializer
from django.http import JsonResponse
import time
import random


class QueryView(APIView):
    def post(self, request):
        serializer = CadastralQuerySerializer(data=request.data)
        if serializer.is_valid():
            # Эмуляция отправки запроса на внешний сервер
            time.sleep(random.randint(1, 60))
            result = random.choice([True, False])
            serializer.save(result=result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultView(APIView):
    def get(self, request, pk):
        try:
            query = CadastralQuery.objects.get(pk=pk)
        except CadastralQuery.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CadastralQuerySerializer(query)
        return Response(serializer.data)


class HistoryView(APIView):
    def get(self, request):
        queries = CadastralQuery.objects.all()
        serializer = CadastralQuerySerializer(queries, many=True)
        return Response(serializer.data)


class HistoryByCadastralNumberView(APIView):
    def get(self, request, cadastral_number):
        queries = CadastralQuery.objects.filter(cadastral_number=cadastral_number)
        serializer = CadastralQuerySerializer(queries, many=True)
        return Response(serializer.data)


class PingView(APIView):
    def get(self, request):
        return Response({"status": "pong"}, status=status.HTTP_200_OK)
