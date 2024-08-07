from django.urls import path
from .views import (
    QueryView,
    ResultView,
    HistoryView,
    HistoryByCadastralNumberView,
    PingView,
)

app_name = "api"

urlpatterns = [
    path("query", QueryView.as_view(), name="query"),
    path("result/<int:pk>", ResultView.as_view(), name="result"),
    path("history", HistoryView.as_view(), name="history"),
    path(
        "history/<str:cadastral_number>",
        HistoryByCadastralNumberView.as_view(),
        name="history_by_cadastral_number",
    ),
    path("ping", PingView.as_view(), name="ping"),
]
