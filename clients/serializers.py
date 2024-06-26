from rest_framework import serializers

from clients.models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ("id", 'full_name', 'email', 'phone', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Client(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
