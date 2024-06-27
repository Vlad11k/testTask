from datetime import datetime

from rest_framework import serializers

from clients.models import Client
from tasks.models import Task


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "client", "employee", "date_create", "date_update", "date_end", "status", "report")
        read_only_fields = ['employee', 'status', 'date_end', 'report']


class TaskAcceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "client", "employee", "date_create", "date_update", "date_end", "status", "report")
        read_only_fields = ['client', 'status', 'date_end']

    def update(self, instance, validated_data):
        if validated_data and instance.status != Task.COMPLETED:
            instance.employee = validated_data.get('employee')
            instance.status = Task.PROCESS
            instance.save()
        return instance


class TaskEndSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "client", "employee", "date_create", "date_update", "date_end", "status", "report")
        read_only_fields = ['client', 'employee', 'status', 'date_end']

    def update(self, instance, validated_data):
        if validated_data and instance.status != Task.COMPLETED:
            instance.report = validated_data.get('report')
            instance.date_end = datetime.now()
            instance.status = Task.COMPLETED
            instance.save()
        return instance