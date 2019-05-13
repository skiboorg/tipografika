# Generated by Django 2.1.4 on 2019-05-13 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customuser.Manager', verbose_name='Ведущий менеджер'),
        ),
    ]
