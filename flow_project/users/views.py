from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

# Представления для регистрации и авторизации
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Используем reverse_lazy для отложенного вычисления URL
    template_name = 'users/signup.html'