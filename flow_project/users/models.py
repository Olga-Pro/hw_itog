from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Поле ID автоматически добавляется Django как Primary Key
    first_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')

    def __str__(self):
        return self.username