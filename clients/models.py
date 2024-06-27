from users.models import User


class Client(User):

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"
