from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Pago
from .serializers import PagoSerializer

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
