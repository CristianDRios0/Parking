from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteListCreateAPIView(APIView):
    
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ClienteDetailAPIView(APIView):
    
    def get(self, request, identificacion):
        cliente = get_object_or_404(Cliente, identificacion=identificacion)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
    
    def put(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
