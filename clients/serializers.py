from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ("id", 'full_name', 'email', 'phone',)
