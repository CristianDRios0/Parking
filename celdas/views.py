from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect, get_object_or_404
from celdas.forms import CeldaForm
from .models import Celda
from .serializers import CeldaSerializer
from django.contrib.auth.decorators import login_required

class CeldaListCreateAPIView(APIView):

    def get(self, request):
            estado = request.GET.get("estado")

            if estado:
                estado = estado.lower().capitalize()  # Normaliza el estado
                if estado in ["Libre", "Ocupado", "Reservado"]:  
                    celdas = Celda.objects.filter(estado=estado)
                else:
                    return Response({"error": "Estado no válido"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                celdas = Celda.objects.all()  # Si no hay filtro, obtiene todas

            serializer = CeldaSerializer(celdas, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CeldaSerializer(data=request.data)  # Recibe datos de una nueva celda
        if serializer.is_valid():
            serializer.save()  # Guarda la celda en la base de datos
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CeldaDetailAPIView(APIView):

    def get(self, request, pk):
        celda = get_object_or_404(Celda, pk=pk)
        serializer = CeldaSerializer(celda)
        return Response(serializer.data)

    def put(self, request, pk):
        celda = get_object_or_404(Celda, pk=pk)
        serializer = CeldaSerializer(celda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        celda = get_object_or_404(Celda, pk=pk)
        celda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required 
def celdas_view(request):
    estado = request.GET.get("estado")
    if estado:
        estado = estado.lower().capitalize()
        celdas = Celda.objects.filter(estado=estado)
    else:
        celdas = Celda.objects.all()

    form = CeldaForm()

    return render(request, 'celdas/listado_celdas.html', {'celdas': celdas, 'form': form})

@login_required   
def crear_celda_view(request):
    if request.method == 'POST':
        form = CeldaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('celdas_view')
    else:
        form = CeldaForm()

    return redirect('celdas_view')