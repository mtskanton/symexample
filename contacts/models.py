from django.db import models
from customers.models import Customer


class Contact(models.Model):
    DEPARTMENTS = (
        ('development', 'разработки'),
        ('supply', 'снабжение'),
        ('marketing', 'маркетинг'),
        ('management', 'управление'),
        ('production', 'производство'),
        ('sales', 'продажи'),
    )
    name = models.CharField(max_length=255, verbose_name='имя')
    surname = models.CharField(max_length=255, blank=True, null=True, verbose_name='фамилия')
    department = models.CharField(max_length=12, blank=True, null=True, choices=DEPARTMENTS, verbose_name='отдел')
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='должность')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='телефон')
    phone_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='телефон 2')
    email = models.CharField(max_length=255, blank=True, null=True, verbose_name='почта')
    email_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='почта 2')
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL,  verbose_name='клиент')
    actual = models.BooleanField(default=True, verbose_name='актуальный')
    emailing = models.BooleanField(default=True, verbose_name='рассылка')
    created = models.DateField(auto_now_add=True, verbose_name='дата добавления')
    updated = models.DateField(auto_now=True, verbose_name='дата обновления')
    comment = models.CharField(max_length=255, blank=True, null=True, verbose_name='комментарий')

    @property
    def display(self):
        surname = self.surname if self.surname else ''
        return f"{self.name} {surname}"

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = 'Контакт клиента'
        verbose_name_plural = 'Контакты клиента'

        permissions = (
            ("manage_contact", "Can manage contact"),
        )

