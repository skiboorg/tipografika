# Generated by Django 2.1.4 on 2019-04-19 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
    ]
