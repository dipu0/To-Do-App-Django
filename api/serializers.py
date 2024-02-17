# api/serializers.py
from rest_framework import serializers
from todolistapp.models import Task, Device

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'complete', 'created']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'user', 'device_token', 'device_type', 'active']