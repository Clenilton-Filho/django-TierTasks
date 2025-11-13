# TierTasks

Pequeno projeto Django para gerenciar uma lista de tarefas com níveis de prioridade e autenticação de usuários.

## Resumo
- Linguagem: Python
- Framework: Django
- Banco de dados: PostgreSQL

## Funcionalidades principais
- Registro de usuário
- Login / Logout (usa as views built-in do Django)
- Criar, remover, marcar como completa/incompleta, adicionar prazo e editar informações das tarefas
- Alternar tarefas entre prioridades
- Opções de filtro e ordenação

## Rotas principais 
- `/` - Página principal (lista de tarefas; criação de novas tarefas via POST)
- `/register/` - Registrar novo usuário
- `/login/` - Login 
- `/logout/` - Logout
- `/toggle/<task_id>/` - Alternar estado de conclusão de tarefas (POST via botão)
- `/delete/<task_id>/` - Apagar uma tarefa
- `/priority/<task_id>/` - Alterna flag de prioridade

## Como rodar o projeto

- principais comandos: 
    
    - python -m venv .venv
    
    
    - .venv/Scripts/activate
    
    
    - cd nome-do-projeto (ex: django-TiestTasks-main)
    
    
    - pip install -r requirements.txt
    
    
    - python manage.py runserver 
    ### obs: necesário obter a .env do projeto

## Navegação e Funcionalidades
- Página de login
    
    
    - fazer login de usuário (campos para inserir nome e senha de uma conta já existente).
    
    
    - botão  'Entrar' para acessar a página principal.
    
    
    - botão 'Criar conta' para acessar a página de registro.


- Página de Registro
    
    
    - instruções na página para criar um usuário corretamente.
    
    
    - fazer registro de novo usuário (campos para inserir nome, senha, e confirmar senha do usuário).
    
    
    - botão 'Criar conta' para concluir registro de usuário.
    
    
    - botão 'Voltar ao login' para voltar à tela inicial.

- Página principal

    - criar tarefas: definir um nome, data, prioridade, e descrição da tarefa.

    - editar tarefas: editar quaisquer informações definidas na criação da tarefa.

    - pesquisa por tarefas: campo de pesquisa/filtragem de tarefas por texto (nome da tarefa).

    - fazer logout da conta.