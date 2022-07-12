from django.db import models
from users.models import User


class Customer(models.Model):
    COUNTRIES = (
        ('ru', 'Россия'),
        ('by', 'Беларусь'),
        ('ua', 'Украина'),
        ('az', 'Азербайджан'),
        ('am', 'Армения'),
        ('kz', 'Казахстан'),
        ('uz', 'Узбекистан'),
        ('md', 'Молдавия'),
    )
    title = models.CharField(max_length=255, verbose_name='название')
    priority = models.BooleanField(default=False, verbose_name='приоритет')
    country = models.CharField(max_length=2, blank=True, null=True, choices=COUNTRIES, default='ru', verbose_name='страна')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='адрес')
    address_2 = models.CharField(max_length=255, blank=True, null=True, verbose_name='адрес 2')
    website = models.CharField(max_length=255, blank=True, null=True, verbose_name='сайт')
    sap = models.CharField(max_length=255, blank=True, null=True, verbose_name='SAP')
    responsible = models.ForeignKey(User, on_delete=models.PROTECT, related_name='customer_responsible', verbose_name='ответственный')
    created = models.DateField(auto_now_add=True, verbose_name='дата добавления')
    updated = models.DateField(auto_now=True, verbose_name='дата обновления')
    comment = models.TextField(blank=True, null=True, verbose_name='комментарий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

        permissions = (
            ("manage_customer", "Can manage customer"),
        )
