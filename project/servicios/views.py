from django.shortcuts import render
from .models import Servicio, Cliente, Pedido


def index(request):
    return render(request, 'servicios/index.html')

def cliente_list(request):
    query = Cliente.objects.all()
    context = {"object_list": query}
    return render(request, 'servicios/cliente_list.html', context)

def servicio_list(request):
    query = Servicio.objects.all()
    context = {"object_list": query}
    return render(request, 'servicios/servicio_list.html', context)

def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, 'servicios/pedido_list.html', context)
