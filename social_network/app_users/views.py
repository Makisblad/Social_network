from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login,logout

def test(request):
    return render(request, "app_users/test.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            login(request, user)
            return redirect('test')#здесь нужно делать редирект на свою страницу
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'app_users/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('test')#здесь нужно делать редирект на свою страницу
    else:
        form = UserLoginForm()
    return render(request, 'app_users/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')
