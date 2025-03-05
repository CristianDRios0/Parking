from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Parqueo
from .serializers import ParqueoSerializer

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
