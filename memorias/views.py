from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm, LoginForm


def chatBot_view(request):
    return render(request, 'chatBot.html')




# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/chatBot')  # Redireciona para a página principal após registo
    else:
        form = SignUpForm()
    return render(request, 'signUp.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/chatBot')  # Redireciona após login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})