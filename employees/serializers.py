from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    # photo = serializers.ImageField(allow_empty_file=False,
    #                                use_url=True,
    #                                required=True,
    #                                label='Фото')

    class Meta:
        model = Employee
        fields = ("id", 'full_name', 'email', 'phone', 'password',)

    def create(self, validated_data):
        user = Employee(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
