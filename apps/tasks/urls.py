from django.urls import path
from apps.tasks.views.tag_views import *

urlpatterns = [
    path('tags/', TagListCreateAPIView.as_view(), name='tag-list-create'), # http://127.0.0.1:8000/api/v1/tasks/tags/
    path('tags/<int:pk>/', TagDetailUpdateDeleteAPIView.as_view(), name='tag-detail-update-delete'), # http://127.0.0.1:8000/api/v1/tasks/tags/1/
]