from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from agile_project.paginations import TasksPagination
from apps.tasks.serializers.task_serializers import ListTaskSerializer, CreateUpdateTaskSerializer, DetailTaskSerializer
from apps.tasks.models import Task

class TaskListCreateView(ListCreateAPIView):
    pagination_class = TasksPagination

    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListTaskSerializer
        return CreateUpdateTaskSerializer

class TaskDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DetailTaskSerializer
        return CreateUpdateTaskSerializer