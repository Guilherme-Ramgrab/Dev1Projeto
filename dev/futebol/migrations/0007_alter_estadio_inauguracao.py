# Generated by Django 4.2.3 on 2023-11-28 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0006_alter_estadio_inauguracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadio',
            name='inauguracao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 9, 32, 53, 620780), help_text='Escolha uma data e hora', verbose_name='Data de Inauguração'),
        ),
    ]