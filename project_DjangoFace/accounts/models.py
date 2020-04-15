from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext, gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(
        'Логин',
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),

        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    email = models.EmailField(verbose_name="Адрес электронной почты", unique=True, max_length=200)
    number = models.CharField("Номер удостоверения", max_length=100)
    is_active = models.BooleanField(('Активный пользователь'), default=False)


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('suspect_detail', kwargs={'pk': self.pk})


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'