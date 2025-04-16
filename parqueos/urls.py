from django.urls import path
from .views import ParqueoListCreateAPIView, ParqueoDetailAPIView, crear_parqueo, formulario_pago, formulario_parqueo

urlpatterns = [
    path('', ParqueoListCreateAPIView.as_view(), name='parqueo-list-create'),
    path('<str:placa>/', ParqueoDetailAPIView.as_view(), name='parqueo-detail'),
    path('formulario/<int:celda_id>/', formulario_parqueo, name='formulario_parqueo'),
    path('crear/<int:celda_id>/', crear_parqueo, name='crear_parqueo'),
    path('formulario-pago/<int:parqueo_id>/', formulario_pago, name='formulario_pago'),
]