from django.shortcuts import render
from AppEntrega.models import Curso


# Create your views here.
def cursos(request):
    all_cursos = Curso.objects.all()
    context = {
        "cursos" : all_cursos
    }
    return render(request, "AppEntrega/cursos.html",context=context)

def crear_curso(request, nombre, camada):
    save_curso = Curso(nombre=nombre, camada=int(camada))
    save_curso.save()
    context = {
        "nombre" : nombre
    }
    return render(request, "AppEntrega/crear_cursos.html",context)

def estudiantes(request):
    return render(request, "base.html")


def profesores(request):
    return render(request, "base.html")
