from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import Curso


# Create your views here.
def guardar_curso(request, camada):
    curso = Curso(nombre="Python", camada=camada)
    curso.save()
    return HttpResponse("Valor Almacenado Exitosamente")
