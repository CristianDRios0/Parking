from django.urls import path
from parqueos.views import formulario_pago
from .views import PagoListCreateAPIView, PagoDetailAPIView, crear_pago

urlpatterns = [
    path('', PagoListCreateAPIView.as_view(), name='pago-list-create'),
    path('<int:pk>/', PagoDetailAPIView.as_view(), name='pago-detail'),
    path('crear/<int:parqueo_id>/', crear_pago, name='crear_pago'),
]