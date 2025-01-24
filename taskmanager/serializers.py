from rest_framework import serializers
from tasks.models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'difficulty']
        