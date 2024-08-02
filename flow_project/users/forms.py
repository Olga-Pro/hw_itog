from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'phone', 'address', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Данный email уже используется.")
        return email