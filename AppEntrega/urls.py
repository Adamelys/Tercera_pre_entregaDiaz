from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('cursos', cursos),
    path('estudiantes', estudiantes),
    path('profesores', profesores),
]
