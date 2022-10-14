from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def test(request):
    return render(request, "app_users/test.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('test')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'app_users/register.html', {'form': form})
def login(request):
    pass
