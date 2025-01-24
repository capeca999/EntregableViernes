from tasks.models import Tasks

from rest_framework import viewsets, permissions
from serializers import TasksSerializer
class TaskViewSet(viewsets.ModelViewSet):
   queryset = Tasks.objects.all()
   permissions_classes = [permissions.AllowAny]
   serializer_class = TasksSerializer
