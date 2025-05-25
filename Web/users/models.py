from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Дополнительные поля
    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'