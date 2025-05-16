from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, pin, name, age, **extra_fields):
        if not phone_number:
            raise ValueError("O número de telefone é obrigatório.")
        if not pin:
            raise ValueError("O PIN é obrigatório.")
        user = self.model(phone_number=phone_number, name=name, age=age, **extra_fields)
        user.set_password(pin)  # encripta o PIN
        user.save()
        return user

    def create_superuser(self, phone_number, pin, name="Admin", age=99, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, pin, name, age, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'age']

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.name} ({self.phone_number})"