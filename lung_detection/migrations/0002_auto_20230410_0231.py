# Generated by Django 3.2 on 2023-04-10 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lung_detection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='prediction_paramenter',
        ),
        migrations.AddField(
            model_name='images',
            name='prediction_paramester',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]