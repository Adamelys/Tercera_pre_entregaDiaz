from django import forms
from django.forms import IntegerField
from chat.models import Chat

class ChatForm(forms.ModelForm):
    usuario     = forms.CharField(min_length=1, max_length=30)
    fecha_hora  = forms.DateField()
    id_mensaje  = forms.IntegerField()
    conversacion= forms.CharField(min_length=1, max_length=250)

    class Meta:
        model = Chat
        fields = ("usuario", "fecha_hora", "id_mensaje", "conversacion")

class consulta_chat(forms.Form):
    usuario = forms.CharField(min_length=1, max_length=30)
    fecha_hora = forms.DateField()
    id_mensaje = forms.IntegerField()
    conversacion = forms.CharField(min_length=1, max_length=250)