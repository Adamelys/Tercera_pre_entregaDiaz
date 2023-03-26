from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('cursos',cursos,name="AppCoderCursos"),
    path('cursos/crear',crear_curso,name="AppCoderCrearCurso"),
    path('buscar_curso',busqueda_curso,name="AppCoderBuscarCurso"),
    path('cursos/Editar/<camada>',editar_curso,name="AppCoderEditarCurso"),
    path('cursos/Eliminar/<camada>',eliminar_curso,name="AppCoderEliminarCurso"),
    path('curso/<nombre>/<camada>',crear_curso1,name="AppCoderCurso"),
    path('estudiantes',estudiantes,name="AppCoderEstudiantes"),
    path('profesores',profesores,name="AppCoderProfesores"),
]
