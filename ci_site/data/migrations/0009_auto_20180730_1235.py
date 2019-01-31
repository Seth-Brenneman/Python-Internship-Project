# Generated by Django 2.0.5 on 2018-07-30 17:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_defect_day_of_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defect',
            name='defect',
        ),
        migrations.RemoveField(
            model_name='defect',
            name='description',
        ),
        migrations.RemoveField(
            model_name='defect',
            name='line',
        ),
        migrations.RemoveField(
            model_name='defect',
            name='station',
        ),
        migrations.AddField(
            model_name='defect',
            name='event',
            field=models.CharField(choices=[('Warranty', 'Warranty'), ('Scrap', 'Scrap'), ('Rework', 'Rework'), ('Delay', 'Delay'), ('Reject', 'Reject')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='defect',
            name='plant',
            field=models.CharField(choices=[('Williams', 'Williams'), ('Cheyenne', 'Cheyenne'), ('Tomahawk', 'Tomahawk')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='defect',
            name='value_stream',
            field=models.CharField(choices=[('VS1', 'VS1'), ('VSO', 'VSO'), ('VSS', 'VSS'), ('VSRV', 'VSRV'), ('VSQ', 'VSQ')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='defect',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2018, 7, 30, 12, 35, 15, 99891), null=True),
        ),
        migrations.AlterField(
            model_name='defect',
            name='day_of_week',
            field=models.CharField(default='Monday', max_length=10),
        ),
    ]