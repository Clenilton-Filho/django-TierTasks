from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'task_list'

# URL patterns da aplicação
# o 'app_name' referencia
# rotas com o nome 'task_list: nome_da_rota' nos templates/views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),

    # Login/Logout usam as views prontas do django
    # Aqui passamos o template que queremos usar para o form de login
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # LogoutView por padrão faz GET, mas configuramos next_page para redirecionar
    path('logout/', auth_views.LogoutView.as_view(next_page='task_list:login'), name='logout'),

    # Rotas que recebem um 'task_id' para mudar o estado da tarefa
    path('toggle/<int:task_id>/', views.toggle_complete, name='toggle_complete'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),

    # Endpoint para obter/atualizar o título e a descrição da tarefa dentro do modal
    path('update/<int:task_id>/', views.update_task, name='update_task'),
]
