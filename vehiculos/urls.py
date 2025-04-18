from django.urls import path
from .views import VehiculoListCreateAPIView, VehiculoDetailAPIView, formulario_vehiculo, crear_vehiculo

urlpatterns = [
    path('', VehiculoListCreateAPIView.as_view(), name='vehiculo-list-create'),
    path("formulario-vehiculo/", formulario_vehiculo, name="formulario_vehiculo"),
    path("crear/", crear_vehiculo, name="crear_vehiculo"),
    path('<str:placa>/', VehiculoDetailAPIView.as_view(), name='vehiculo-detail'),
]