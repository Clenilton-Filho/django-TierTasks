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
        due = request.POST.get('due', '').strip()
        priority = request.POST.get('priority', '').strip()  # opções: '', 'low', 'medium', 'high'
        if title:
            if Task.objects.filter(owner=request.user, title__iexact=title).exists():
                messages.error(request, 'Tarefa com esse título já existe.')
                return redirect('task_list:home')

            # Analisar data de prazo opcional usando parse_date que
            # retorna uma date ou None. Se a data for inválida, informa o usuário.
            due_date = None
            if due:
                parsed = parse_date(due)
                if not parsed:
                    messages.error(request, 'Formato de prazo inválido. Use AAAA-MM-DD.')
                    return redirect('task_list:home')
                due_date = parsed

            # validar prioridade (básico) aceitando apenas as strings padrão
            if priority not in ('', Task.PRIORITY_LOW, Task.PRIORITY_MEDIUM, Task.PRIORITY_HIGH):
                priority = ''

            Task.objects.create(owner=request.user, title=title, due_date=due_date, priority_level=priority)
            messages.success(request, 'Tarefa adicionada.')
            return redirect('task_list:home')
        else:
            messages.error(request, 'Por favor preencha o campo da tarefa.')

    # Consulta base: somente tarefas do usuário
    qs = Task.objects.filter(owner=request.user)

    # Filtragem: permitimos parâmetros via querystring para facilitar uso sem JS
    # filter_opt: pode ser 'all', 'completed', 'incomplete'
    filter_opt = request.GET.get('filter', 'all')

    # Busca de texto simples (por título completo ou parcial). Substitui o antigo
    # filtro/agrupar rápido por letra. Nome do parâmetro: `q`.
    q = request.GET.get('q', '').strip()

    # Detectando se o formulário de filtro (o controle) foi submetido. Adicionamos um
    # input escondido 'filter_action' ao formulário para distinguir um usuário
    # que está mudando o filtro de um envio normal de busca.
    filter_action = request.GET.get('filter_action')

    # Se o usuário escolheu 'all' no controle de filtro, tratando isso como
    # um pedido para reverter filtros incluindo qualquer busca de texto e ignorando 'q'
    if filter_opt == 'all' and filter_action:
        q = ''

    if filter_opt == 'completed':
        qs = qs.filter(completed=True)
    elif filter_opt == 'incomplete':
        qs = qs.filter(completed=False)

    # Aplicar busca de texto
    if q:
        qs = qs.filter(title__icontains=q)

    # Opções de ordenação
    sort = request.GET.get('sort', 'date_desc')
    if sort == 'date_asc':
        order_fields = ['due_date', 'created_at']
    elif sort == 'title_asc':
        order_fields = ['title']
    elif sort == 'title_desc':
        order_fields = ['-title']
    elif sort == 'due_asc':
        # Ordenação simples por data (pode colocar valores nulos primeiro dependendo do banco)
        order_fields = ['due_date', 'created_at']
    elif sort == 'due_desc':
        order_fields = ['-due_date', 'created_at']
    elif sort == 'priority':
        # Ordenação simples pela string priority_level (menos precisa que um rank numérico)
        order_fields = ['priority_level', '-created_at']
    else:
        order_fields = ['-created_at']

    qs = qs.order_by(*order_fields)

    # Separando listas por nível de prioridade
    high_tasks = list(qs.filter(priority_level=Task.PRIORITY_HIGH))
    medium_tasks = list(qs.filter(priority_level=Task.PRIORITY_MEDIUM))
    low_tasks = list(qs.filter(priority_level=Task.PRIORITY_LOW))

    # Tasks sem prioridade (mostradas na seção 'Sem prioridade' sem agrupamento)
    none_tasks = list(qs.filter(priority_level=''))

    # Atribui um índice sequencial de exibição para todas as tarefas visíveis para a interface
    # mostrar, por exemplo, "Tarefa #1, #2..." que renumera quando tarefas são removidas.
    counter = 1
    for lst in (high_tasks, medium_tasks, low_tasks, none_tasks):
        for t in lst:
            try:
                setattr(t, 'display_index', counter)
            except Exception:
                # defensivo: se por algum motivo definir atributo falhar, pule
                pass
            counter += 1

    context = {
        'high_tasks': high_tasks,
        'medium_tasks': medium_tasks,
        'low_tasks': low_tasks,
        'none_tasks': none_tasks,
        'sort': sort,
        'filter': filter_opt,
        'q': q,
    }
    return render(request, 'task_list/home.html', context)


# Apenas POST com redirect (sem AJAX/JSON) para tornar o fluxo mais simples
@login_required
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)

    if request.method != 'POST':
        # Requisições que não forem POST redirecionam de volta para a home
        return redirect('task_list:home')

    # Ler dados do formulário
    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    due = request.POST.get('due', '').strip()
    priority = request.POST.get('priority', '').strip()

    if not title:
        messages.error(request, 'Título é obrigatório.')
        return redirect('task_list:home')

    # Verifica duplicidade (ignorando a própria tarefa)
    if Task.objects.filter(owner=request.user, title__iexact=title).exclude(id=task.id).exists():
        messages.error(request, 'Tarefa com esse título já existe.')
        return redirect('task_list:home')

    task.title = title
    task.description = description

    # Validando a data (que é opcional)
    if due:
        parsed = parse_date(due)
        if not parsed:
            messages.error(request, 'Formato de prazo inválido.')
            return redirect('task_list:home')
        task.due_date = parsed
    else:
        task.due_date = None

    # Validando e atribuindo priority_level
    if priority not in ('', Task.PRIORITY_LOW, Task.PRIORITY_MEDIUM, Task.PRIORITY_HIGH):
        priority = ''
    task.priority_level = priority

    task.save()
    messages.success(request, 'Tarefa atualizada.')
    return redirect('task_list:home')


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
    return render(request, 'task_list/register.html', {'form': form})


@login_required
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.completed = not task.completed
    task.save()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer or 'task_list:home')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    task.delete()
    messages.success(request, 'Tarefa apagada.')
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer or 'task_list:home')
