# Generated by Django 2.0 on 2019-06-07 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0014_auto_20190530_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dhis_disease_data_values',
            old_name='data_element_uid',
            new_name='data_element_id',
        ),
        migrations.RenameField(
            model_name='dhis_disease_data_values',
            old_name='dhis_disease',
            new_name='dhis_reported_disease_id',
        ),
        migrations.RenameField(
            model_name='dhis_event_data_values',
            old_name='data_element_uid',
            new_name='data_element_id',
        ),
        migrations.RenameField(
            model_name='dhis_event_data_values',
            old_name='dhis_event',
            new_name='dhis_reported_event_id',
        ),
        migrations.RenameField(
            model_name='dhis_reported_diseases',
            old_name='org_unit_uid',
            new_name='org_unit_id',
        ),
        migrations.RenameField(
            model_name='dhis_reported_events',
            old_name='org_unit_uid',
            new_name='org_unit_id',
        ),
        migrations.RemoveField(
            model_name='idsr_weekly_report',
            name='idsr_disease_uid',
        ),
        migrations.RemoveField(
            model_name='idsr_weekly_report',
            name='idsr_incident_uid',
        ),
        migrations.RemoveField(
            model_name='idsr_weekly_report',
            name='org_unit_uid',
        ),
        migrations.AddField(
            model_name='idsr_weekly_report',
            name='idsr_disease_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='veoc.idsr_diseases'),
        ),
        migrations.AddField(
            model_name='idsr_weekly_report',
            name='idsr_incident_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='veoc.idsr_reported_incidents'),
        ),
        migrations.AddField(
            model_name='idsr_weekly_report',
            name='org_unit_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='veoc.organizational_units'),
        ),
    ]
