# Generated by Django 3.1.5 on 2021-01-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20210106_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tnx_no',
            field=models.CharField(default='2979597337', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]