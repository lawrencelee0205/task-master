from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

    class Meta:
        model = Task
        fields = ('id', 'name', 'description')

    