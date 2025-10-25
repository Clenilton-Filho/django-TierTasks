# TierTasks

Pequeno projeto Django para gerenciar uma lista de tarefas com níveis de prioridade e autenticação de usuários.

Resumo
- Linguagem: Python
- Framework: Django
- Banco de dados:

Funcionalidades principais
- Registro de usuário
- Login / Logout (usa as views built-in do Django)
- Criar, remover, marcar como completa/incompleta, adicionar prazo e editar informações das tarefas
- Alternar tarefas entre prioridades
- Opções de filtro e ordenação

Rotas principais 
- `/` - Página principal (lista de tarefas; criação de novas tarefas via POST)
- `/register/` - Registrar novo usuário
- `/login/` - Login 
- `/logout/` - Logout
- `/toggle/<task_id>/` - Alternar estado de conclusão de tarefas (POST via botão)
- `/delete/<task_id>/` - Apagar uma tarefa
- `/priority/<task_id>/` - Alterna flag de prioridade