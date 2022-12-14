# Generated by Django 4.1.1 on 2022-10-05 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('guruh', models.CharField(blank=True, max_length=50)),
                ('st_raqam', models.PositiveIntegerField(blank=True)),
                ('tel', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='Student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.student'),
        ),
    ]
