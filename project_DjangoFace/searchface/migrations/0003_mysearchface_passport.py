# Generated by Django 3.0.5 on 2020-04-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchface', '0002_mysearchface_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mysearchface',
            name='passport',
            field=models.CharField(default=2, max_length=12, verbose_name='Паспорт'),
            preserve_default=False,
        ),
    ]