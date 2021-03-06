# Generated by Django 4.0.6 on 2022-07-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('archive', models.BooleanField(verbose_name='архив')),
                ('created', models.DateField(auto_now_add=True, verbose_name='дата добавления')),
                ('updated', models.DateField(auto_now=True, verbose_name='дата обновления')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='контакт')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.customer', verbose_name='клиент')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]
