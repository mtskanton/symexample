from django.db import models
from users.models import User
from customers.models import Customer
from contacts.models import Contact
from projects.models import Project
from products.models import Product


class Task(models.Model):
    description = models.TextField(blank=True, verbose_name='описание')
    result = models.TextField(blank=True, null=True, verbose_name='результат')
    created = models.DateField(auto_now_add=True, verbose_name='дата добавления')
    updated = models.DateField(auto_now=True, verbose_name='дата обновления')
    reminder = models.DateField(blank=True, null=True, verbose_name='дата напоминания')
    done = models.BooleanField(default=False, verbose_name='выполнено')
    done_date = models.DateField(blank=True, null=True, verbose_name='дата выполнения')
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_creator', verbose_name='создатель')
    responsible = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_responsible', verbose_name='ответственный')
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE, verbose_name='клиент')
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='контакт')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.CASCADE, verbose_name='проект')
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='продукт')

    @property
    def display(self):
        if len(self.description) > 20:
            return self.description[0:20] + '...'
        return self.description

    @property
    def result_short(self):
        if self.result and len(self.result) > 20:
            return self.result[0:20] + '...'
        return self.result

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

        permissions = (
            ("manage_task", "Can manage task"),
        )
