from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.models import User

# Форма регистрации
class CustomUserCreationForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Введите имя')
    # email = forms.EmailField(max_length=254, required=True, help_text='Укажите корректный email.')
    # phone = forms.CharField(max_length=15, required=True)
    # address = forms.CharField(max_length=255, required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'email', 'phone', 'address', 'password1', 'password2')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if CustomUser.objects.filter(username=username).exists():
    #         raise forms.ValidationError("Пользователь с таким именем уже существует.")
    #     return username

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'email', 'phone', 'address', 'password1', 'password2']
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if CustomUser.objects.filter(email=email).exists():
#             raise forms.ValidationError("Данный email уже используется.")
#         return email