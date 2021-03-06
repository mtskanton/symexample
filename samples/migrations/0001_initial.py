# Generated by Django 4.0.6 on 2022-07-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='количество')),
                ('status', models.CharField(choices=[('to_get', 'получить'), ('to_send', 'отправить'), ('on_testing', 'на тестировании'), ('approved', 'одобрен'), ('win', 'win (есть заказ)'), ('not_actual', 'не актуален'), ('declined_by_properties', 'отклонен по свойствам'), ('declined_by_price', 'отклонен по цене')], default='to get', max_length=25, verbose_name='статус')),
                ('status_date', models.DateField(blank=True, null=True, verbose_name='дата статуса')),
                ('direct', models.BooleanField(default=False, verbose_name='напрямую')),
                ('important', models.BooleanField(default=False, verbose_name='значимый')),
                ('potential', models.CharField(blank=True, max_length=255, null=True, verbose_name='потенциал')),
                ('pace', models.CharField(blank=True, max_length=255, null=True, verbose_name='pace')),
                ('sent', models.DateField(blank=True, null=True, verbose_name='дата отправки')),
                ('sent_data', models.CharField(blank=True, max_length=255, null=True, verbose_name='данные отправки')),
                ('created', models.DateField(auto_now_add=True, verbose_name='дата добавления')),
                ('updated', models.DateField(auto_now=True, verbose_name='дата обновления')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='контакт')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='клиент')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='продукт')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.project', verbose_name='проект')),
            ],
            options={
                'verbose_name': 'Образец',
                'verbose_name_plural': 'Образцы',
                'permissions': (('manage_sample', 'Can manage sample'),),
            },
        ),
    ]
