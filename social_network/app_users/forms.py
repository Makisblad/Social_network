from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import User
from django import forms
from .widgets import DatePickerInput

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Ник', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    # first_name = forms.CharField(label='Имя', widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
    # last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
    # birth_date = forms.DateField(label='Дата рождения', widget=DatePickerInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'birth_date',  'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
