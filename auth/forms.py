from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Введите email')
    password1 = forms.CharField(help_text=None,
                                label='Придумайте пароль',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(help_text=None,
                                label='Подтвердите пароль',
                                widget=forms.PasswordInput())
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email уже существует")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    class Meta:
        model = User
        fields = ("email", "password1", "password2", )

class AuthForm(AuthenticationForm):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ("email", "password", )