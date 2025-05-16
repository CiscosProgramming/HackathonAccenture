from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
from django.contrib import messages

from .models import *

def chatBot_view(request):
    return render(request, 'chatBot.html')

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        phone_number = request.POST.get('phoneNumber')
        idade = request.POST.get('idade')
        pin = request.POST.get('pin')

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'Número de telefone já cadastrado.')
            return render(request, 'signup.html')

        try:
            idade_int = int(idade)
        except (ValueError, TypeError):
            messages.error(request, 'Idade inválida.')
            return render(request, 'signup.html')

        user = CustomUser.objects.create_user(
            phone_number=phone_number,
            pin=pin,
            name=nome,
            age=idade_int
        )

        login(request, user, backend='memorias.auth_backend.PhoneNumberBackend')
        return redirect(reverse('memorias:chatBot'))

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        pin = request.POST.get('pin')

        print(f"Tentando autenticar: phone_number={phone_number}, pin={pin}")
        user = authenticate(request, phone_number=phone_number, pin=pin)
        print(f"Usuário autenticado: {user}")

        user = authenticate(request, phone_number=phone_number, pin=pin)
        if user is not None:
            login(request, user)
            return redirect('memorias:chatBot')  
        else:
            messages.error(request, 'Número de telemóvel ou PIN inválido.')
            return render(request, 'login.html')

    return render(request, 'login.html')