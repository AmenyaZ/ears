# Generated by Django 3.0.6 on 2020-06-19 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0083_auto_20200616_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discharged_quarantine',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 726765)),
        ),
        migrations.AlterField(
            model_name='home_based_care',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 725767)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 722775)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='source',
            field=models.CharField(default='Web Registration', max_length=50),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 722775)),
        ),
        migrations.AlterField(
            model_name='quarantine_follow_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 722775)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 725767)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_lab_confirmation',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 725767)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_collected',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 725767)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_taken_lab',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 725767)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 26, 46, 725767)),
        ),
    ]