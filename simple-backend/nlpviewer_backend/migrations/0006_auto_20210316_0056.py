# Generated by Django 3.1.6 on 2021-03-16 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlpviewer_backend', '0005_auto_20210307_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotationlog',
            name='endTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 0, 56, 39, 300487)),
        ),
        migrations.AlterField(
            model_name='annotationlog',
            name='startTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 16, 0, 56, 39, 300434)),
        ),
    ]
