from django.urls import path
from .views import TarifaListCreateAPIView, TarifaDetailAPIView

urlpatterns = [
    path('tarifas/', TarifaListCreateAPIView.as_view(), name='tarifa-list-create'),
    path('tarifas/<int:pk>/', TarifaDetailAPIView.as_view(), name='tarifa-detail'),
]