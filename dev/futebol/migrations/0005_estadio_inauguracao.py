# Generated by Django 4.2.3 on 2023-11-14 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0004_alter_estadio_cod'),
    ]

    operations = [
        migrations.AddField(
            model_name='estadio',
            name='inauguracao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 14, 10, 8, 48, 52373), help_text='Escolha uma data e hora', verbose_name='Data de Inauguração'),
        ),
    ]
