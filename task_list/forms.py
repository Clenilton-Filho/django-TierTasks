from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulário de registro estendendo UserCreationForm para uso simples
# usando o formulário pronto do django,
# que já valida username e senha
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):

        # Salva o usuário
        return super().save(commit=commit)
