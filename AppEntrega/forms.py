from django import forms
from AppEntrega.models import Curso, Estudiantes, Profesor

class CursoForm(forms.ModelForm):
    # nombre = forms.CharField(min_length=3,id_mensaje)
    # camada = forms.IntegerField(min_value=100)
    class Meta:
        model = Curso
        fields = "__all__"

class Estudiantesform(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = "__all__"

class Profesorform(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = "__all__"

class BusquedaCursoForm(forms.Form):
    nombre = forms.CharField(min_length=3,max_length=40)

