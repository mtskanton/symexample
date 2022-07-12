from django.db import models
from products.models import Product
from customers.models import Customer
from contacts.models import Contact
from projects.models import Project


class Sample(models.Model):
    STATUSES = (
        ('to_get', 'получить'),
        ('to_send', 'отправить'),
        ('on_testing', 'на тестировании'),
        ('approved', 'одобрен'),
        ('win', 'win (есть заказ)'),
        ('not_actual', 'не актуален'),
        ('declined_by_properties', 'отклонен по свойствам'),
        ('declined_by_price', 'отклонен по цене'),
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='продукт')
    amount = models.IntegerField(verbose_name='количество')
    status = models.CharField(max_length=25, choices=STATUSES, default='to get', verbose_name='статус')
    status_date = models.DateField(blank=True, null=True, verbose_name='дата статуса')
    direct = models.BooleanField(default=False, verbose_name='напрямую')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='клиент')
    contact = models.ForeignKey(Contact, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='контакт')
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='проект')
    important = models.BooleanField(default=False, verbose_name='значимый')
    potential = models.CharField(max_length=255, blank=True, null=True, verbose_name='потенциал')
    pace = models.CharField(max_length=255, blank=True, null=True, verbose_name='pace')
    sent = models.DateField(blank=True, null=True, verbose_name='дата отправки')
    sent_data = models.CharField(max_length=255, blank=True, null=True, verbose_name='данные отправки')
    created = models.DateField(auto_now_add=True, verbose_name='дата добавления')
    updated = models.DateField(auto_now=True, verbose_name='дата обновления')
    comment = models.TextField(blank=True, null=True, verbose_name='комментарий')

    @property
    def display(self):
        return 'образец ' + self.product.display

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = 'Образец'
        verbose_name_plural = 'Образцы'

        permissions = (
            ("manage_sample", "Can manage sample"),
        )
