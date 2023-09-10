# Generated by Django 4.2 on 2023-04-30 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=1000000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=1000)),
                ('room', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='messenger',
        ),
    ]
