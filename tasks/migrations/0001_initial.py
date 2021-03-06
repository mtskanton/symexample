# Generated by Django 4.0.6 on 2022-07-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contacts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('result', models.TextField(blank=True, null=True, verbose_name='результат')),
                ('created', models.DateField(auto_now_add=True, verbose_name='дата добавления')),
                ('updated', models.DateField(auto_now=True, verbose_name='дата обновления')),
                ('reminder', models.DateField(blank=True, null=True, verbose_name='дата напоминания')),
                ('done', models.BooleanField(default=False, verbose_name='выполнено')),
                ('done_date', models.DateField(blank=True, null=True, verbose_name='дата выполнения')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.contact', verbose_name='контакт')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
                'permissions': (('manage_task', 'Can manage task'),),
            },
        ),
    ]
