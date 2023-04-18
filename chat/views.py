from django.shortcuts import render, redirect
from chat.forms import ChatForm, buscar_chat
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
            return redirect("account/form.html")

    context = {
        "form": ChatForm()
    }
    return render(request,"AppEntrega/chat.html",context=context)

def consulta_chat(request):
    #mostrar datos filtrados
    mi_formulario = buscar_chat(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        consulta_chat = Chat.objects.all()

        context = {
            "chat": consulta_chat
        }

    return render(request,"AppEntrega/chat.html",context=context)

def blog(request):

    return render(request,"AppEntrega/blog.html")