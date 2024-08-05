from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


#
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# from .forms import CustomUserCreationForm
#
# # Представления для регистрации и авторизации
# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')  # Используем reverse_lazy для отложенного вычисления URL
#     template_name = 'users/signup.html'