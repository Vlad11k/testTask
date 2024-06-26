from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

