from django.utils import timezone
import math
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from celdas.models import Celda
from parqueos.forms import ParqueoForm
from .models import Parqueo
from .serializers import ParqueoSerializer
from django.views.decorators.cache import never_cache

class ParqueoListCreateAPIView(APIView):

    def get(self, request):
        parqueos = Parqueo.objects.all()
        serializer = ParqueoSerializer(parqueos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParqueoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ParqueoDetailAPIView(APIView):
    
    def get(self, request, placa):
        parqueo = get_object_or_404(Parqueo, vehiculo__placa=placa)
        serializer = ParqueoSerializer(parqueo)
        return Response(serializer.data)

    def put(self, request, placa):
        parqueo = get_object_or_404(Parqueo, vehiculo__placa=placa)
        serializer = ParqueoSerializer(parqueo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, placa):
        parqueo = get_object_or_404(Parqueo, vehiculo__placa=placa)
        parqueo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@never_cache
@login_required
def formulario_parqueo(request, celda_id):
    celda = get_object_or_404(Celda, id=celda_id)
    form = ParqueoForm()
    return render(request, 'parqueos/formulario_parqueo.html', {'form': form, 'celda': celda})

@never_cache
@login_required
def crear_parqueo(request, celda_id):
    celda = get_object_or_404(Celda, id=celda_id)

    if request.method == 'POST':
        form = ParqueoForm(request.POST)
        if form.is_valid():
            parqueo = form.save(commit=False)
            parqueo.celda = celda
            parqueo.estado = 'activo'
            parqueo.save()

            celda.estado = 'ocupado'
            celda.save()

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

@never_cache      
@login_required
def formulario_pago(request, parqueo_id):
    parqueo = get_object_or_404(Parqueo, pk=parqueo_id, estado='activo')

    # Calculamos tiempo y total como en la vista de crear
    tiempo = timezone.now() - parqueo.fecha_entrada
    horas = math.ceil(tiempo.total_seconds() / 3600)
    monto = horas * parqueo.tarifa.monto

    return render(request, 'pagos/formulario_pago.html', {
        'parqueo': parqueo,
        'monto': monto
    })