from django.db import models

from users.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


