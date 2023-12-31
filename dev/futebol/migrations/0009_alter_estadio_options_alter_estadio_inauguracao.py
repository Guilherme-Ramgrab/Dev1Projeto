# Generated by Django 4.2.7 on 2023-11-28 21:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0008_alter_estadio_inauguracao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estadio',
            options={'permissions': {('reserve_estadio', 'can reserve Estadios')}},
        ),
        migrations.AlterField(
            model_name='estadio',
            name='inauguracao',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 18, 49, 31, 760781), help_text='Escolha uma data e hora', verbose_name='Data de Inauguração'),
        ),
    ]
