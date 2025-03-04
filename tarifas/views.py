from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tarifa
from .serializers import TarifaSerializer

class TarifaListCreateAPIView(APIView):

    def get(self, request):
        tarifas = Tarifa.objects.all()
        serializer = TarifaSerializer(tarifas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TarifaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TarifaDetailAPIView(APIView):
    
    def get(self, request, pk):
        tarifa = get_object_or_404(Tarifa, pk=pk)
        serializer = TarifaSerializer(tarifa)
        return Response(serializer.data)

    def put(self, request, pk):
        tarifa = get_object_or_404(Tarifa, pk=pk)
        serializer = TarifaSerializer(tarifa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarifa = get_object_or_404(Tarifa, pk=pk)
        tarifa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
