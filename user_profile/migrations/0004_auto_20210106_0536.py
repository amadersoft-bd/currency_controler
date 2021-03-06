# Generated by Django 3.1.5 on 2021-01-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20210106_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tnx_no',
            field=models.CharField(default='8650351679', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
