from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from clientes.models import Cliente
from vehiculos.forms import VehiculoForm
from .models import Vehiculo
from .serializers import VehiculoSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

class VehiculoListCreateAPIView(APIView):

    def get(self, request):
        vehiculos = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VehiculoDetailAPIView(APIView):
    
    def get(self, request, placa):
        vehiculo = get_object_or_404(Vehiculo, placa=placa)
        serializer = VehiculoSerializer(vehiculo)
        return Response(serializer.data)

    def put(self, request, placa):
        vehiculo = get_object_or_404(Vehiculo, placa=placa)
        serializer = VehiculoSerializer(vehiculo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, placa):
        vehiculo = get_object_or_404(Vehiculo, placa=placa)
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@never_cache
@login_required   
def formulario_vehiculo(request):
    clientes = Cliente.objects.all()
    return render(request, "vehiculos/formulario_vehiculo.html", {"clientes": clientes})

@never_cache
@login_required 
def crear_vehiculo(request):
    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "errors": form.errors})
