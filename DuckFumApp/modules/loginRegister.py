from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_user(request, username, password):
    # Autentica al usuario y lo inicia en la sesión
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        return False