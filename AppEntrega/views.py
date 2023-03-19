from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import Curso


# Create your views here.
def cursos(request):
    return render(request, "index.html")


def estudiantes(request):
    return render(request, "index.html")


def profesores(request):
    return render(request, "index.html")
