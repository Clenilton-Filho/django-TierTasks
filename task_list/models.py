from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    # Cada tarefa pertence a um usuário
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)

    # Descrição da tarefa (opcional)
    description = models.TextField(blank=True, default='')

    # Prazo para a tarefa (opcional)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    # Prioridade entre 'low', 'medium', 'high' (obrigatório)
    PRIORITY_LOW = 'low'
    PRIORITY_MEDIUM = 'medium'
    PRIORITY_HIGH = 'high'
    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Baixa'),
        (PRIORITY_MEDIUM, 'Média'),
        (PRIORITY_HIGH, 'Alta'),
    ]
    priority_level = models.CharField(max_length=6, choices=PRIORITY_CHOICES, blank=False, default=PRIORITY_MEDIUM)

    def __str__(self):
        return f"{self.title} ({'done' if self.completed else 'todo'})"
