from django.db import models
from django.contrib.auth.models import AbstractUser


class Organisation(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,  verbose_name='управление')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, error_messages={"unique": "A user with that username already exists."})
    organisation = models.ForeignKey(Organisation, null=True, on_delete=models.PROTECT, verbose_name='организация')

    @property
    def display(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
