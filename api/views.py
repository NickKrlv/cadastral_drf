from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import CadastralQuery
from .serializers import CadastralQuerySerializer
import time
import random


class QueryView(generics.CreateAPIView):
    queryset = CadastralQuery.objects.all()
    serializer_class = CadastralQuerySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Эмуляция отправки запроса на внешний сервер
            time.sleep(random.randint(1, 60))
            result = random.choice([True, False])
            serializer.save(result=result)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResultView(generics.RetrieveAPIView):
    queryset = CadastralQuery.objects.all()
    serializer_class = CadastralQuerySerializer


class HistoryView(generics.ListAPIView):
    queryset = CadastralQuery.objects.all()
    serializer_class = CadastralQuerySerializer


class HistoryByCadastralNumberView(generics.ListAPIView):
    serializer_class = CadastralQuerySerializer

    def get_queryset(self):
        cadastral_number = self.kwargs["cadastral_number"]
        return CadastralQuery.objects.filter(cadastral_number=cadastral_number)


class PingView(APIView):
    def get(self, request):
        return Response({"status": "pong"}, status=status.HTTP_200_OK)
