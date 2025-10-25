from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    # Cada tarefa pertence a um usuário
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)

    # Descrição opcional da tarefa. Não é preenchida na criação, apenas no modo de edição
    description = models.TextField(blank=True, default='')

    # Prazo opcional para a tarefa. Armazenamos apenas a data
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    # prioridade é um nível: '', 'low', 'medium', 'high'
    PRIORITY_LOW = 'low'
    PRIORITY_MEDIUM = 'medium'
    PRIORITY_HIGH = 'high'
    PRIORITY_CHOICES = [
        ('', 'Sem prioridade'),
        (PRIORITY_LOW, 'Baixa'),
        (PRIORITY_MEDIUM, 'Média'),
        (PRIORITY_HIGH, 'Alta'),
    ]
    priority_level = models.CharField(max_length=6, choices=PRIORITY_CHOICES, blank=True, default='')

    def __str__(self):
        return f"{self.title} ({'done' if self.completed else 'todo'})"
