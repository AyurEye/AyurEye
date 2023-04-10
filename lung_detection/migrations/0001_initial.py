# Generated by Django 3.2 on 2023-04-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('x_ray', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('disease_detected', models.BooleanField(blank=True, null=True)),
                ('prediction_image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('prediction_paramenter', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
