from django.urls import path, include
from chat.views import *
from django.contrib import admin

urlpatterns = [
    path('chat/', chatusers, name="chatusers"),
]