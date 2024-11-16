# Generated by Django 5.1.3 on 2024-11-10 12:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='password',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='signup_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]