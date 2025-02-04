# Generated by Django 5.0.7 on 2024-07-17 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_todolist'),
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.todolist'),
        ),
    ]
