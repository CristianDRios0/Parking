from django.urls import path
from .views import VehiculoListCreateAPIView, VehiculoDetailAPIView

urlpatterns = [
    path('vehiculos/', VehiculoListCreateAPIView.as_view(), name='vehiculo-list-create'),
    path('vehiculos/<str:placa>/', VehiculoDetailAPIView.as_view(), name='vehiculo-detail'),
]