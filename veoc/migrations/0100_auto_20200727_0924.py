# Generated by Django 2.0 on 2020-07-27 06:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veoc', '0099_auto_20200718_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='airline_quarantine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(blank=True, max_length=100)),
                ('flight_number', models.CharField(blank=True, max_length=200)),
                ('seat_number', models.CharField(blank=True, max_length=200)),
                ('destination_city', models.CharField(blank=True, max_length=200)),
                ('travel_history', models.CharField(blank=True, max_length=200)),
                ('residence', models.CharField(blank=True, max_length=200)),
                ('postal_address', models.CharField(blank=True, max_length=200)),
                ('estate', models.CharField(blank=True, max_length=200)),
                ('cough', models.BooleanField(default=True)),
                ('breathing_difficulty', models.BooleanField(default=True)),
                ('fever', models.BooleanField(default=True)),
                ('chills', models.BooleanField(default=True)),
                ('temperature', models.FloatField(blank=True, default='0.0', max_length=200)),
                ('measured_temperature', models.FloatField(blank=True, default='0.0', max_length=200)),
                ('arrival_airport_code', models.CharField(blank=True, max_length=200)),
                ('released', models.BooleanField(default=True)),
                ('risk_assessment_referal', models.BooleanField(default=True)),
                ('designated_hospital_refferal', models.BooleanField(default=True)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 705546))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 705546))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='airline_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='api_access_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 685654)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 685654)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='date_tested',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 685654)),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='result',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='covid_results',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 685654)),
        ),
        migrations.AlterField(
            model_name='discharged_quarantine',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 688591)),
        ),
        migrations.AlterField(
            model_name='home_based_care',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 688591)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 681669)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 681669)),
        ),
        migrations.AlterField(
            model_name='quarantine_follow_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 682607)),
        ),
        migrations.AlterField(
            model_name='quarantine_revisit',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 684602)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 687594)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_lab_confirmation',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 687594)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_collected',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 687594)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='onset_of_symptoms',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 687594)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 9, 24, 13, 687594)),
        ),
        migrations.AddField(
            model_name='airline_quarantine',
            name='patient_contacts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='airline_contact', to='veoc.quarantine_contacts'),
        ),
        migrations.AddField(
            model_name='airline_quarantine',
            name='updated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='airline_created_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
