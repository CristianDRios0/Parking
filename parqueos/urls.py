from django.urls import path
from .views import ParqueoListCreateAPIView, ParqueoDetailAPIView

urlpatterns = [
    path('parqueos/', ParqueoListCreateAPIView.as_view(), name='parqueo-list-create'),
    path('parqueos/<str:placa>/', ParqueoDetailAPIView.as_view(), name='parqueo-detail'),
]