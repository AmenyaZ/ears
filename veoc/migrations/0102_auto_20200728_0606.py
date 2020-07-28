# Generated by Django 3.0.6 on 2020-07-28 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0101_auto_20200728_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airline_quarantine',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 333734)),
        ),
        migrations.AlterField(
            model_name='airline_quarantine',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 333734)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='api_access_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 312789)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 311790)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='date_tested',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 311790)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 312789)),
        ),
        migrations.AlterField(
            model_name='discharged_quarantine',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 314781)),
        ),
        migrations.AlterField(
            model_name='home_based_care',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 314781)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 308320)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 308320)),
        ),
        migrations.AlterField(
            model_name='quarantine_follow_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 308767)),
        ),
        migrations.AlterField(
            model_name='quarantine_revisit',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 311790)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 313879)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_lab_confirmation',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 313879)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_collected',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 313879)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='onset_of_symptoms',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 313879)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 28, 6, 6, 37, 313879)),
        ),
    ]
