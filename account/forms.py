from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    if_staff = forms.BooleanField()
    class Meta:
        model = User
        fields = ("username", "email", "if_staff")
