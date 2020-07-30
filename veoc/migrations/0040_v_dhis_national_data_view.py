# Generated by Django 2.0 on 2019-08-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0039_auto_20190828_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='v_dhis_national_data_view',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('period', models.CharField(max_length=100)),
                ('value', models.FloatField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'v_dhis_national_data_view',
            },
        ),
    ]
