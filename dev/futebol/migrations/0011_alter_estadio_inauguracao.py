# Generated by Django 4.2.3 on 2023-12-05 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0010_alter_estadio_inauguracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadio',
            name='inauguracao',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 10, 53, 55, 761444), help_text='Escolha uma data e hora', verbose_name='Data de Inauguração'),
        ),
    ]
