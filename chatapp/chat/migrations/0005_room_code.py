# Generated by Django 4.2 on 2023-04-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_message_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]