from django.shortcuts import render
from .models import Servicio

def home(request):
    # Traemos solo los 3 servicios principales para el inicio
    servicios = Servicio.objects.all()[:3]
    return render(request, 'web/index.html', {'servicios': servicios})

def nosotros(request):
    return render(request, 'web/nosotros.html')

def servicios(request):
    todos_servicios = Servicio.objects.all().order_by('orden')
    return render(request, 'web/servicios.html', {'servicios': todos_servicios})

def contacto(request):
    return render(request, 'web/contacto.html')