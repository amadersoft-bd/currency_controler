# Generated by Django 3.1.5 on 2021-01-17 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
    ]