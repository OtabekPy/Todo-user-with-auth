# Generated by Django 4.1.1 on 2022-10-05 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_todo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]