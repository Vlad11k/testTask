# Generated by Django 5.0.6 on 2024-06-27 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='report',
            field=models.TextField(default=None, verbose_name='Отчёт'),
        ),
    ]
