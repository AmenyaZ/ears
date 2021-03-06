# Generated by Django 3.0.6 on 2020-06-11 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0081_auto_20200611_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck_quarantine_lab',
            name='sample_identifier',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 584211)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 584211)),
        ),
        migrations.AlterField(
            model_name='quarantine_follow_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 584211)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 587203)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_lab_confirmation',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 587203)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_collected',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 587203)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_taken_lab',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 587203)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 7, 26, 45, 587203)),
        ),
    ]
