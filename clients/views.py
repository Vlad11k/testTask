from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from clients.models import Client
from clients.permissions import IsOwner, IsEmployee
from clients.serializers import ClientSerializer


class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsEmployee, )


class ClientAPIRetrieve(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsEmployee, )


class ClientAPIProfile(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        client = self.request.user
        if client.is_authenticated:
            return Client.objects.filter(user_ptr=client)
        return self.permission_denied(self.request)
