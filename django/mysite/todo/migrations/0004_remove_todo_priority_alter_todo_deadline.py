# Generated by Django 4.2.4 on 2023-08-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='priority',
        ),
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateField(),
        ),
    ]
