"""
URL configuration for Parking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    #path('', redirect_to_admin),
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('celdas/', include('celdas.urls')),
    path('parqueos/', include('parqueos.urls')),
    path('api/celdas/', include('celdas.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/tarifas/', include('tarifas.urls')),
    path('api/vehiculos/', include('vehiculos.urls')),
    path('api/parqueos/', include('parqueos.urls')),
    path('api/pagos/', include('pagos.urls')),
]
