from django.test import TestCase
from django.urls import reverse

from AppEntrega.models import Curso


# Create your tests here.
class CursoTestCase(TestCase):
    def SetUp(self):
        Curso.objects.create(nombre="Python1",camada=10000)
        Curso.objects.create(nombre="Python2", camada=20000)

    def test_creando_cursos(self):
        p1 = Curso.objects.get(camada=10000)
        p2 = Curso.objects.get(camada=20000)
        self.assertEqual(p1.nombre, "Python1")
        self.assertEqual(p2.nombre, "Python2")

class ViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('AppCoderCursos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Creacion del curso")

    def test_past_question(self):
        curso = Curso.objects.create(nombre="Python1", camada=10000)
        response = self.client.get(reverse('AppCoderCursos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f"curso:Python1 camada:10000"
        )