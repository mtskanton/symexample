from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from contacts.models import Contact


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='клиент')
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='контакт')
    archive = models.BooleanField(verbose_name='архив')
    created = models.DateField(auto_now_add=True, verbose_name='дата добавления')
    updated = models.DateField(auto_now=True, verbose_name='дата обновления')

    @property
    def display(self):
        if len(self.title) > 20:
            return self.title[0:20] + '...'
        return self.title

    @property
    def description_short(self):
        if self.description and len(self.description) > 20:
            return self.description[0:20] + '...'
        return self.description

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
