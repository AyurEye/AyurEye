# Generated by Django 3.2 on 2023-04-10 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lung_detection', '0002_auto_20230410_0231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='prediction_paramester',
            new_name='prediction_parameter',
        ),
    ]