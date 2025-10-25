from django.contrib import admin
from .models import Task

# Registrando o modelo de tarefa no admin do django
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    # Campos mostrados na lista do admin
    list_display = ('title', 'owner', 'completed', 'priority_display', 'created_at')

    # Filtros para facilitar encontrar tarefas por estado
    list_filter = ('completed', 'priority_level')

    # Campos pesquisáveis na interface do admin
    search_fields = ('title', 'owner__username')

    def priority_display(self, obj):
        if obj.priority_level == 'high':
            return 'Alta'
        if obj.priority_level == 'medium':
            return 'Média'
        if obj.priority_level == 'low':
            return 'Baixa'
        return 'Sem prioridade'
    priority_display.short_description = 'Prioridade'
