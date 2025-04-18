from django.utils import timezone
import math
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.decorators.cache import never_cache
from parqueos.models import Parqueo
from .models import Pago
from .serializers import PagoSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

class PagoListCreateAPIView(APIView):
    
    def get(self, request):
        pagos = Pago.objects.all()
        serializer = PagoSerializer(pagos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PagoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PagoDetailAPIView(APIView):

    def get(self, request, pk):
        pago = get_object_or_404(Pago, pk=pk)
        serializer = PagoSerializer(pago)
        return Response(serializer.data)

    def put(self, request, pk):
        pago = get_object_or_404(Pago, pk=pk)
        serializer = PagoSerializer(pago, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        pago = get_object_or_404(Pago, pk=pk)
        pago.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@never_cache
@require_POST
def crear_pago(request, parqueo_id):
    parqueo = get_object_or_404(Parqueo, id=parqueo_id)

    # Registrar fecha de salida
    parqueo.fecha_salida = timezone.now()

    # Calcular tiempo y total
    tiempo = parqueo.fecha_salida - parqueo.fecha_entrada
    horas = math.ceil(tiempo.total_seconds() / 3600)
    total = horas * parqueo.tarifa.monto
    parqueo.total_pagado = total
    parqueo.estado = 'finalizado'
    parqueo.save()

    # Registrar pago
    Pago.objects.create(
        parqueo=parqueo,
        cliente=parqueo.vehiculo.cliente,
        monto=total
    )

    # Liberar celda
    celda = parqueo.celda
    celda.estado = 'libre'
    celda.save()

    return JsonResponse({'success': True})