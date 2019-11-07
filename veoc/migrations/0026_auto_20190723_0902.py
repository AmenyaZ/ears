# Generated by Django 2.0 on 2019-07-23 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0025_auto_20190716_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='case_status',
            field=models.BooleanField(choices=[(1, 'Open'), (2, 'Closed')], default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='case_status',
            field=models.BooleanField(choices=[(1, 'Open'), (2, 'Closed')], default=1),
        ),
    ]