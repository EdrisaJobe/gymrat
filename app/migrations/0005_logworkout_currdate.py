# Generated by Django 3.2.5 on 2022-03-21 16:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220319_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='logworkout',
            name='currdate',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
