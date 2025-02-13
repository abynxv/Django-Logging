from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .logging_utils import log_execution_time, logger



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @log_execution_time
    def list(self, request):
        logger.info('Retrieving all tasks', extra={'user': request.user.username if request.user.is_authenticated else 'anonymous'})
        return super().list(request)

    @log_execution_time
    def create(self, request):
        logger.info('Creating new task', extra={'task_data': request.data})
        return super().create(request)

    @log_execution_time
    def update(self, request, *args, **kwargs):
        task = self.get_object()
        logger.info(
            'Updating task',
            extra={
                'task_id': task.id,
                'old_data': TaskSerializer(task).data,
                'new_data': request.data
            }
        )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        task = self.get_object()
        logger.warning(
            'Deleting task',
            extra={
                'task_id': task.id,
                'task_data': TaskSerializer(task).data
            }
        )
        return super().destroy(request, *args, **kwargs)