from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from django.db.models import UniqueConstraint

User = get_user_model()


class Request(models.Model):
    """Модель заявки."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Заявитель',
        related_name='request'
    )
    theme = models.CharField(
        verbose_name='Тема заявки',
        max_length=100
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message=
        "Номер телефона необходимо "
        "ввести в формате: '+999999999'."
        "Допускается до 15 цифр."
    )
    phone_number = models.CharField(
        verbose_name='Номер телефона',
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'{self.user}, {self.theme}'


class RequestMessage(models.Model):
    """Модель сообщения."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='requestmessage',
        verbose_name='Автор сообщения к заявке'
    )
    message = models.CharField(
        verbose_name='Текст сообщения',
        max_length=300
    )
    request = models.ForeignKey(
        Request,
        on_delete=models.CASCADE,
        related_name='requestmessage'
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return f'{self.message}'
