from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from auth1.forms import RegisterForm, AuthForm
# from django.contrib.auth import get_user_model
# User = get_user_model()

# class CustomLoginView(LoginView):
#     authentication_form = AuthForm
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print(form)
        if form.is_valid():
            print('form_valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print('if user')
                # login(request, user, backend='auth1.auth_backends.UserEmailBackend')
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                print('wronng 1')
                messages.error(request, "Invalid username or password.")
        else:
            print('wrong 2')
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    print('form 2', form)
    return render(request,
                  "registration/login.html",
                  context={"form":form})

# def home(request):
#     return render(
#         request,
#         'home.html'
#     )


def logout_request(request):
    logout(request)
    return render(
        request,
        'registration/logout.html'
    )


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(request, email=email, password=raw_password)
            user = form.save()
            # login(request, user, backend='auth1.auth_backends.UserEmailBackend')
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})
