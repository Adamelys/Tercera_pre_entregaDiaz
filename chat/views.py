from django.shortcuts import render, redirect
from chat.forms import ChatForm
from AppEntrega.forms import CursoForm, BusquedaCursoForm
from AppEntrega.models import Curso
from chat.models import Chat

# Create your views here.

def chatusers(request):
    if request.method == "POST":
        mi_formulario = ChatForm(request.POST)

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            chat_save = Chat(
                fecha_hora = informacion['fecha_hora'],
                usuario = informacion['usuario'],
                id_mensaje = informacion['id_mensaje'],
                conversacion = informacion['conversacion']
            )
            mi_formulario.save()
            return render(request,"AppEntrega/chat.html")

    context = {
        "form": ChatForm()
    }
    return render(request,"AppEntrega/chat.html",context=context)
