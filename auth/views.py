from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from auth.forms import RegisterForm, AuthForm


class CustomLoginView(LoginView):
    authentication_form = AuthForm


def home(request):
    return render(
        request,
        'home.html'
    )


def logout(request):
    return render(
        request,
        'registration/logout.html'
    )


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})
