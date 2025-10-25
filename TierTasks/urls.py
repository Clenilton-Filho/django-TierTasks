from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Incluindo as urls do app para os templates poderem usar reverse com task_list:...
    path('', include('task_list.urls', namespace='task_list')),
]
