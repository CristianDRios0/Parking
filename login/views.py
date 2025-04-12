from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/')  # o a otra vista que definas como dashboard
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login/login.html')
