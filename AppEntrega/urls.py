from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('cursos', cursos,name="AppCoderCursos"),
    path('curso/<nombre>/<camada>', crear_curso,name="AppCoderCurso"),
    path('estudiantes', estudiantes,name="AppCoderEstudiantes"),
    path('profesores', profesores,name="AppCoderProfesores"),
]
