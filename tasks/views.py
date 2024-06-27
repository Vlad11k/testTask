from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from employees.models import Employee
from tasks.models import Task
from tasks.permissions import IsOwner
from tasks.serializers import TaskListSerializer, TaskAcceptSerializer, TaskEndSerializer


class TaskAPIList(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()

        try:
            user = self.request.user.employee
        except:
            user = self.request.user.client
        if type(user) == Employee:
            return Task.objects.filter(status=Task.WAITING) | Task.objects.filter(employee_id=user.pk)
        elif type(user) == Client:
            return Task.objects.filter(client_id=user.pk)


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAcceptSerializer
    permission_classes = (IsOwner, )


class TaskAPIEnd(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskEndSerializer

    permission_classes = (IsOwner,)
