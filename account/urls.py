from django.urls import path, include
from django.contrib import admin
from account.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_account,name="accountlogin"),
    path('registrar/',register_account,name="accountregister"),
    path('editar/usuario/', editar_usuario, name="accounteditarusuario"),
    path('logout/',LogoutView.as_view(template_name="account/logout.html"),name="accountlogout"),
]