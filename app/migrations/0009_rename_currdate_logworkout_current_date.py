# Generated by Django 3.2.5 on 2022-03-21 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_logworkout_currdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logworkout',
            old_name='currdate',
            new_name='current_date',
        ),
    ]
