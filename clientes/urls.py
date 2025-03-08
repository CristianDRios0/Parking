from django.urls import path
from .views import ClienteListCreateAPIView, ClienteDetailAPIView

urlpatterns = [
    path('clientes/', ClienteListCreateAPIView.as_view(), name='cliente-list-create'),
    path('clientes/<str:identificacion>/', ClienteDetailAPIView.as_view(), name='cliente-detail'),
]