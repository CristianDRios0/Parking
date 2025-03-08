from django.urls import path
from .views import PagoListCreateAPIView, PagoDetailAPIView

urlpatterns = [
    path('pagos/', PagoListCreateAPIView.as_view(), name='pago-list-create'),
    path('pagos/<int:pk>/', PagoDetailAPIView.as_view(), name='pago-detail'),
]