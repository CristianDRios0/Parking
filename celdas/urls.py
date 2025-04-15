from django.urls import path
from .views import CeldaListCreateAPIView, CeldaDetailAPIView, celdas_view, crear_celda_view

urlpatterns = [
    path('', CeldaListCreateAPIView.as_view(), name='celda-list-create'),
    path('<int:pk>/', CeldaDetailAPIView.as_view(), name='celda-detail'),
    path('vista/', celdas_view, name='celdas_view'),
    path('crear/', crear_celda_view, name='crear_celda'),
]