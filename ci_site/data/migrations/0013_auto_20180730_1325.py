# Generated by Django 2.0.5 on 2018-07-30 18:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20180730_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 13, 25, 15, 554436), null=True),
        ),
    ]
