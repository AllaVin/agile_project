from django.urls import path, include

urlpatterns = [
    path('tasks/', include('apps.tasks.urls')), # http://127.0.0.1:8000/api/v1/tasks/tags/
    path('projects/', include('apps.projects.urls')),
]
