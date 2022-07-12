from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    CATEGORIES = (
        ('Actives', (
            ('SA', 'Skin Actives'),
            ('HA', 'Hair Actives'),
        )),
        ('MicroProtection', (
            ('SP', 'Skin Protection'),
            ('PP', 'Product Protection'),
        )),
        ('Sun&Fun', (
            ('SUN', 'Sun Care'),
            ('FUN', 'Functionals'),
        )),
        ('Botanicals&Colors', (
            ('BOT', 'Botanicals'),
            ('COL', 'Colors'),
        ))
    )
    SANCTION_STATUS = (
       ('Unknown', 'не проверен'),
       ('True', 'да'),
       ('False', 'нет'),
    )

    category = models.CharField(max_length=3, choices=CATEGORIES, verbose_name='категория')
    subcategory = models.CharField(max_length=255, blank=True, null=True, verbose_name='подкатегория')
    phn = models.CharField(max_length=255, blank=True, null=True, verbose_name='группа')
    priority = models.CharField(max_length=255, blank=True, null=True, verbose_name='приоритет')
    number = models.IntegerField(verbose_name='номер')
    title = models.CharField(max_length=255, verbose_name='название')
    properties = models.TextField(blank=True, null=True, verbose_name='свойства')
    inci = models.TextField(blank=True, null=True, verbose_name='inci')
    dosage = models.CharField(max_length=255, blank=True, null=True, verbose_name='ввод')
    color = models.CharField(max_length=255, blank=True, null=True, verbose_name='цвет')
    form = models.CharField(max_length=255, blank=True, null=True, verbose_name='форма')
    solubility = models.CharField(max_length=255, blank=True, null=True, verbose_name='растворимость')
    registration = models.CharField(max_length=255, blank=True, null=True, verbose_name='регистрация')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    actual = models.BooleanField(default=True, null=True, verbose_name='актуальный')
    sanctioned = models.CharField(max_length=7, choices=SANCTION_STATUS, default='Unknown', verbose_name='санкционный')

    @property
    def display(self):
        return self.title + ' (' + str(self.number) + ')'

    def __str__(self):
        return self.display

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
