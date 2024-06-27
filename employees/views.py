from rest_framework import generics

from employees.models import Employee
from employees.permissions import IsEmployee, IsOwner
from employees.serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated


class EmployeeAPIList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated, )


class EmployeeAPIRetrieve(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsOwner, IsEmployee, )


class EmployeeAPIProfile(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Employee.objects.filter(user_ptr=user)
        return self.permission_denied(self.request)

