from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(allow_empty_file=False,
                                   use_url=True,
                                   required=True,
                                   label='Фото')

    class Meta:
        model = Employee
        fields = ("id", 'full_name', 'email', 'phone', 'photo')
