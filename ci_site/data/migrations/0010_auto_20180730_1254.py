# Generated by Django 2.0.5 on 2018-07-30 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20180730_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AddField(
            model_name='profile',
            name='plant',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Cheyenne'), (2, 'Tomahawk'), (3, 'Williams')], null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='value_stream',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(4, 'VS1'), (5, 'VSO'), (6, 'VSS'), (7, 'VSRV'), (8, 'VSQ')], null=True),
        ),
        migrations.AlterField(
            model_name='defect',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 12, 54, 45, 345475), null=True),
        ),
    ]
