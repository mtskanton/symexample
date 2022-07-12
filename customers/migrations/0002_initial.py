# Generated by Django 4.0.6 on 2022-07-12 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='responsible',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_responsible', to=settings.AUTH_USER_MODEL, verbose_name='ответственный'),
        ),
    ]