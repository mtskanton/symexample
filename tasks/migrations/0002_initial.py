# Generated by Django 4.0.6 on 2022-07-12 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_initial'),
        ('projects', '0001_initial'),
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_creator', to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AddField(
            model_name='task',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='клиент'),
        ),
        migrations.AddField(
            model_name='task',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='продукт'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='проект'),
        ),
        migrations.AddField(
            model_name='task',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='task_responsible', to=settings.AUTH_USER_MODEL, verbose_name='ответственный'),
        ),
    ]
