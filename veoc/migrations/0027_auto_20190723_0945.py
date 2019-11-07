# Generated by Django 2.0 on 2019-07-23 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veoc', '0026_auto_20190723_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='case_status',
            field=models.CharField(choices=[(1, 'Open'), (2, 'Closed')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='case_status',
            field=models.CharField(choices=[(1, 'Open'), (2, 'Closed')], default=1, max_length=10),
        ),
    ]