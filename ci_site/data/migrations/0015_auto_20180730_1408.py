# Generated by Django 2.0.5 on 2018-07-30 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20180730_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 14, 8, 6, 444134), null=True),
        ),
    ]