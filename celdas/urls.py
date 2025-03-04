from django.urls import path
from .views import CeldaListCreateAPIView, CeldaDetailAPIView

urlpatterns = [
    path('celdas/', CeldaListCreateAPIView.as_view(), name='celda-list-create'),
    path('celdas/<int:pk>/', CeldaDetailAPIView.as_view(), name='celda-detail'),
]