from rest_framework import generics

from clients.models import Client
from employees.models import Employee
from tasks.models import Task
from tasks.serializers import TaskListSerializer, TaskAcceptSerializer, TaskEndSerializer


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer

    # def get_queryset(self):
    #     if self.request.user.is_staff:
    #         pass
    #
    #     try:
    #         user = self.request.user.employee
    #     except:
    #         user = self.request.user.client
    #     if type(user) == Employee:
    #         # return Task.objects.filter(employee_id=user.pk)
    #         return Task.objects.filter(status=Task.WAITING)
    #     elif type(user) == Client:
    #         return Task.objects.filter(client_id=user.pk)


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAcceptSerializer


class TaskAPIEnd(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEndSerializer
