from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vehiculo
from .serializers import VehiculoSerializer

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
