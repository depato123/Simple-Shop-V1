from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    first_name = forms.CharField(max_length=30, required=True, label='Nombre real')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name')