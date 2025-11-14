from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import UserRegistrationForm
from django.utils.dateparse import parse_date

@login_required
def home(request):

    # Criação de tarefas
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        due = request.POST.get('due_date', request.POST.get('due', '')).strip()
        priority = request.POST.get('priority_level', request.POST.get('priority', '')).strip()  # opções: 'low', 'medium', 'high'
        description = request.POST.get('description', '').strip()
        if title:
            if Task.objects.filter(owner=request.user, title__iexact=title).exists():
                messages.error(request, 'Tarefa com esse título já existe.')
                return redirect('task_list:home')

            # Prioridade obrigatória
            if priority not in (Task.PRIORITY_LOW, Task.PRIORITY_MEDIUM, Task.PRIORITY_HIGH):
                messages.error(request, 'Prioridade inválida. Escolha Alta, Média ou Baixa.')
                return redirect('task_list:home')

            # Analisar data de prazo opcional usando parse_date que
            # retorna uma date ou None. Se a data não for válida, informa.
            due_date = None
            if due:
                parsed = parse_date(due)
                if not parsed:
                    messages.error(request, 'Formato de prazo inválido. Use AAAA-MM-DD.')
                    return redirect('task_list:home')
                due_date = parsed

            # Criando a tarefa
            Task.objects.create(owner=request.user, title=title, due_date=due_date, priority_level=priority, description=description)
            return redirect('task_list:home')
        else:
            messages.error(request, 'Por favor preencha o campo da tarefa.')

    # Consulta base: somente tarefas do usuário
    qs = Task.objects.filter(owner=request.user)

    # Filtragem: permitimos parâmetros via querystring para facilitar uso sem JS
    # filter_opt: pode ser 'all', 'completed', 'incomplete'
    filter_opt = request.GET.get('filter', 'all')

    # Busca de texto simples (por título completo ou parcial). Nome do parâmetro: `q`.
    q = request.GET.get('q', '').strip()

    # Detectando se o formulário de filtro (o controle) foi enviado.
    filter_action = request.GET.get('filter_action')

    if filter_opt == 'all' and filter_action:
        q = ''

    if filter_opt == 'completed':
        qs = qs.filter(completed=True)
    elif filter_opt == 'incomplete':
        qs = qs.filter(completed=False)

    # Aplicar a busca por título
    if q:
        qs = qs.filter(title__icontains=q)

    # Separando listas por nível de prioridade (tiers)
    high_tasks = list(qs.filter(priority_level=Task.PRIORITY_HIGH))
    medium_tasks = list(qs.filter(priority_level=Task.PRIORITY_MEDIUM))
    low_tasks = list(qs.filter(priority_level=Task.PRIORITY_LOW))

    # Quantidade de slots vazios em cada nível (carousel)
    empty_slots_high = range(max(0, 3 - len(high_tasks)))
    empty_slots_medium = range(max(0, 3 - len(medium_tasks)))
    empty_slots_low= range(max(0, 3 - len(low_tasks)))

    # Índice para todas as tarefas
    counter = 1
    for lst in (high_tasks, medium_tasks, low_tasks):
        for t in lst:
            try:
                setattr(t, 'display_index', counter)
            except Exception:
                pass
            counter += 1

    # Lista de todas as tarefas (para os modais)
    tasks = list(high_tasks) + list(medium_tasks) + list(low_tasks)

    context = {
        'high_tasks': high_tasks,
        'medium_tasks': medium_tasks,
        'low_tasks': low_tasks,
        'tasks': tasks,
        'empty_slots_high':empty_slots_high,
        'empty_slots_medium': empty_slots_medium,
        'empty_slots_low': empty_slots_low,
        'q': q,
    }
    return render(request, 'task_list/home.html', context)


# Modificar uma tarefa
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)

    if request.method != 'POST':
        return redirect('task_list:home')

    # Ler dados do formulário
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    due = request.POST.get('due_date', request.POST.get('due', '')).strip()
    priority = request.POST.get('priority_level', request.POST.get('priority', '')).strip()

    if not title:
        messages.error(request, 'Título é obrigatório.')
        return redirect('task_list:home')

    if Task.objects.filter(owner=request.user, title__iexact=title).exclude(id=task.id).exists():
        messages.error(request, 'Tarefa com esse título já existe.')
        return redirect('task_list:home')

    # Prioridade obrigatória
    if priority not in (Task.PRIORITY_LOW, Task.PRIORITY_MEDIUM, Task.PRIORITY_HIGH):
        messages.error(request, 'Prioridade inválida. Escolha Alta, Média ou Baixa.')
        return redirect('task_list:home')

    task.title = title
    task.description = description

    if due:
        parsed = parse_date(due)
        if not parsed:
            messages.error(request, 'Formato de prazo inválido.')
            return redirect('task_list:home')
        task.due_date = parsed
    else:
        task.due_date = None

    task.priority_level = priority

    task.save()
    return redirect('task_list:home')


# Registro de usuário
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Conta criada. Faça login.')
            return redirect('task_list:login')
        else:
            if 'username' in form.errors:
                messages.error(request, 'Nome de usuário já está em uso.')
            if 'password1' in form.errors:
                pw_errs = form.errors.get('password1')
                if pw_errs:
                    messages.error(request, str(pw_errs[0]))
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# Alterar estado da tarefa (concluída, não concluída)
@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.completed = not task.completed
    task.save()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer or 'task_list:home')


# Apagar uma tarefa
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.delete()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer or 'task_list:home')
