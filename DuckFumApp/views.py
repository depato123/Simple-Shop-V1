from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .modules.forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html')

def shop(request):
    return render(request, 'shop.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Recopila la información del formulario
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            password = form.cleaned_data.get('password1')

            # Crea un nuevo usuario en la base de datos
            user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
            user.save()

            # Redirige al usuario a la página principal
            return redirect('/')
    else:
        # Muestra el formulario de registro
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def carrito(request):
    return render(request, 'carrito.html')

def admin(request):
    return render(request, 'admin.html')

def create(request):
    return render(request, 'create.html')

def detalle(request):
    return render(request, 'detalle.html')

