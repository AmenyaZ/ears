# Generated by Django 3.0.6 on 2020-07-02 09:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0091_auto_20200701_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarantine_revisit',
            name='border_point',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='revisit_border_point', to='veoc.border_points'),
        ),
        migrations.AddField(
            model_name='quarantine_revisit',
            name='breathing_difficulty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quarantine_revisit',
            name='cough',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quarantine_revisit',
            name='fever',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quarantine_revisit',
            name='sample_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quarantine_revisit',
            name='temperature',
            field=models.FloatField(blank=True, default='0.0', max_length=50),
        ),
        migrations.AddField(
            model_name='quarantine_revisit',
            name='weighbridge_facility',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='revisit_weighbridge', to='veoc.weighbridge_sites'),
        ),
        migrations.AlterField(
            model_name='discharged_quarantine',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 596475)),
        ),
        migrations.AlterField(
            model_name='home_based_care',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 596475)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 590490)),
        ),
        migrations.AlterField(
            model_name='quarantine_contacts',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 590490)),
        ),
        migrations.AlterField(
            model_name='quarantine_follow_up',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 591461)),
        ),
        migrations.AlterField(
            model_name='quarantine_revisit',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 594481)),
        ),
        migrations.AlterField(
            model_name='quarantine_revisit',
            name='quarantine_site',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='quarantine_revisit_site', to='veoc.quarantine_sites'),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 595477)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_lab_confirmation',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 595477)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='date_specimen_collected',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 595477)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='onset_of_symptoms',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 595477)),
        ),
        migrations.AlterField(
            model_name='truck_quarantine_lab',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 12, 58, 41, 595477)),
        ),
    ]
