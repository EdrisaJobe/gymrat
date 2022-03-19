# Generated by Django 3.2.5 on 2022-03-19 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20220319_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logworkout',
            name='date',
        ),
        migrations.AddField(
            model_name='logworkout',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
