from rest_framework import generics

from clients.models import Client
from clients.permissions import IsEmployee
from clients.serializers import ClientSerializer


class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsEmployee,)


class ClientAPIRetrieve(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsEmployee,)


class ClientAPIProfile(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Client.objects.filter(user_ptr=user)
        return self.permission_denied(self.request)
