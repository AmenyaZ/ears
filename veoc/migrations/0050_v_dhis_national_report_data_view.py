# Generated by Django 2.0 on 2020-01-27 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0049_staff_contact_team_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='v_dhis_national_report_data_view',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('period', models.CharField(max_length=100)),
                ('cases', models.FloatField(max_length=50)),
                ('deaths', models.FloatField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'v_dhis_national_report_data_view',
            },
        ),
    ]
