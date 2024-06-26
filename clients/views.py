from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


