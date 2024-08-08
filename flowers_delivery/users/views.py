from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db import IntegrityError
from .forms import CustomUserCreationForm

import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Регистрация прошла успешно. Теперь вы можете войти.')
                return redirect('login')
            except IntegrityError:
                logger.error('Пользователь с таким именем уже существует.', exc_info=True)
                messages.error(request,'Пользователь с таким именем уже существует.')
        else:
            # Добавьте логирование для отладки
            logger.error('Форма регистрации недействительна: %s', form.errors)
            messages.error(request, 'Возникла ошибка при заполнении формы. Пожалуйста, проверьте введенные данные.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalog')  # или любой другой URL после успешного входа
        else:
            # Обработка ошибки аутентификации
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'users/login.html')
