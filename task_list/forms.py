from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

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

    def clean_password1(self):

         #Exige pelo menos uma letra maiúscula e um número na senha.
         password = self.cleaned_data.get('password1')
         if not password:
             return password

         # Verifica pelo menos uma letra maiúscula
         if not re.search(r'[A-Z]', password):
             raise ValidationError('A senha deve conter ao menos uma letra maiúscula.')

         # Verifica ao menos um dígito
         if not re.search(r'\d', password):
             raise ValidationError('A senha deve conter ao menos um número.')

         return password
