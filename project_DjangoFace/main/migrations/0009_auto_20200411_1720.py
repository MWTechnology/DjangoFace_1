# Generated by Django 3.0.5 on 2020-04-11 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200407_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suspect',
            options={'verbose_name': 'Подозреваемый', 'verbose_name_plural': 'Подозреваемые'},
        ),
    ]
