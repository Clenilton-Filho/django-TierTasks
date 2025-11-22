# <img src="static/images/TierTasks_icon.png" style="height:30px; width: 30px; margin-bottom: -3px"></img> TierTasks

![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-%2306B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

> Aplicação web simples em Django para gerenciar tarefas pessoais organizadas em níveis de prioridade (tiers). O projeto oferece autenticação de usuários, criação/edição/exclusão de tarefas e uma interface responsiva.

---

## 📌 Sobre o Projeto


### ✅ Principais objetivos:

fornecer uma lista de tarefas com foco em prioridade visual (alta / média / baixa) e fluxos básicos de UX (modais, filtros, pesquisa simples).

### 🖥️ Tecnologias:

Python, Django, PostgreSQL, Tailwind CSS.

---

### 👥 Autores

* **Clenilton:** Página principal e configurações básicas.
* **Eduardo:** Elaboração das views principais do projeto.
* **Jonathan:** Integração com banco de dados em nuvem e páginas de Login e Cadastro.

---

## Requisitos mínimos:
- **Python:** 3.10 ou superior
- **Dependências:** especificadas em `requirements.txt`

---

## ⚡ Como Rodar

1) Criar e ativar o ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate
```

2) Instalar dependências:

```powershell
pip install -r requirements.txt
```

3) Rodar migrações:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4) Iniciar o servidor de desenvolvimento:

```powershell
python manage.py runserver
```

Abra `http://127.0.0.1:8000/` no navegador.

---



## 🚀 Uso Rápido

### 📋 Registrar: Crie uma conta na página de registro e acesse via login.

> Os requisitos são para a senha.

<img src="assets/screenshots/registro.png" style="border-radius:10px"></img>

### 🔐 Logar: acesse a conta pela página de login.

<img src="assets/screenshots/login.png" style="border-radius:10px"></img>

### 📊 Dashboard: A página principal exibe suas tarefas organizadas por grupos (tiers) de prioridade (Alta, Média e Baixa).

> Use os botões rápidos no card para marcar como concluída, editar ou excluir a tarefa. 

<img src="assets/screenshots/principal.png" style="border-radius:10px"></img>

### ✏️ Criar Tarefa: Use o botão no cabeçalho ou os slots vazios para abrir o modal de criação. 

> Preencha o título (obrigatório), prioridade (obrigatório), prazo e descrição.

<img src="assets/screenshots/modal_criar_editar.png" style="border-radius:10px"></img>


### 🔍 Pesquisar: O botão de busca no cabeçalho abre um modal para filtrar tarefas pelo título.

> Esvazie para limpar o filtro.

<img src="assets/screenshots/modal_pesquisar.png" style="border-radius:10px"></img>


---

## 🔗 Rotas importantes

- `GET /`  página principal (requer login).
- `GET/POST /register/`  registrar usuário.
- `GET/POST /login/`  login (usa `LoginView` do Django).
- `POST /logout/`  logout (usa `LogoutView` do Django).
- `POST /toggle/<task_id>/`  alterna `completed`.
- `POST /delete/<task_id>/`  deleta tarefa.
- `POST /update/<task_id>/`  atualiza título/descrição/prazo/prioridade.

---

## 📂 Estrutura do Projeto

- `assets/screenshots` : prints das principais telas.
- `static/` : arquivos estáticos (CSS, JS, imagens).
- `task_list/` : app principal.
  - `models.py` : modelo `Task`.
  - `views.py` : lógica das views (home, register, toggle, delete, update).
  - `forms.py` : `UserRegistrationForm` (valida senha).
  - `urls.py` : rotas do app.
  - `templates/task_list/` : template da página principal.
- `templates/` : template `base`.
  - `base.html/` : template `base`.
  - `registration/` : templates de `login` e `register`.
- `TierTasks/` : configurações do projeto.