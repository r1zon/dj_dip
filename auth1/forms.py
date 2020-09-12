from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
# from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.HiddenInput(), required=False)
    email = forms.EmailField(label='Введите email',
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(help_text=None,
                                label='Придумайте пароль',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(help_text=None,
                                label='Подтвердите пароль',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))
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
    username = UsernameField(widget=forms.HiddenInput(), required=False)
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ("email", "password", )