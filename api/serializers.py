# api/serializers.py
from rest_framework import serializers
from todolistapp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete', 'created']
