# Generated by Django 3.2 on 2022-12-09 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cody', '0002_alter_employee_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата рождения'),
        ),
    ]
