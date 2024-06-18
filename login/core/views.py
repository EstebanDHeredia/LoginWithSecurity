from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


@login_required  # Para ingresar a esta vista necesito estar logueado, sino me redirecciona a la pagina de login
def products(request):
    return render(request, 'core/products.html')


def exit(request):
    logout(request)
    return redirect('home')
