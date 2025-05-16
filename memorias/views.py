from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login
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

        login(request, user)
        return redirect(reverse('memorias:chatBot'))

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/chatBot')  # Redireciona após login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})