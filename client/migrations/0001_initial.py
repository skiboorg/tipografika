# Generated by Django 2.1.4 on 2018-12-27 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Имя')),
                ('family', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Фамилия')),
                ('otchesnvo', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Отчество')),
                ('firm', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Фирма')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Телефон')),
                ('is_vip', models.BooleanField(default=False, verbose_name='Вип')),
                ('firm_address', models.TextField(blank=True, default='', null=True, verbose_name='Адрес фирмы')),
                ('personal_address', models.TextField(blank=True, default='', null=True, verbose_name='Личный адрес')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
