from django.db import models

from users.models import User


class Client(User):

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


