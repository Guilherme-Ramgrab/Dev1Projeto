# Generated by Django 4.2.3 on 2023-11-28 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0007_alter_estadio_inauguracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadio',
            name='inauguracao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 10, 42, 30, 994240), help_text='Escolha uma data e hora', verbose_name='Data de Inauguração'),
        ),
    ]
