from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

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

class Calendario(models.Model):
    utilizador = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='calendario')

    def __str__(self):
        return f"Calendário de {self.utilizador.name}"

class Lembrete(models.Model):
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE, related_name='lembretes')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    data_hora = models.DateTimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lembrete: {self.titulo} ({self.data_hora.strftime('%d/%m/%Y %H:%M')})"

class Conversa(models.Model):
    id = models.AutoField(primary_key=True)
    utilizador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='conversas')
    label = models.CharField(max_length=100)
    content = models.TextField()
    source = models.CharField(max_length=10, choices=[('bot', 'ChatBot'), ('user', 'Utilizador')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.label} ({self.timestamp.strftime('%d/%m/%Y %H:%M')})"

class PromptCatalog(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.categoria} - {self.text[:30]}..."