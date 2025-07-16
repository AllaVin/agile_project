from django.urls import path
from apps.projects.views.project_views import *

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='project-list-create')  # http://127.0.0.1:8000/api/v1/projects/?date_from=2024-01-01&date_to=2026-01-01
]